(ns advent-of-code-2020.day-10
  (:require [clojure.test :refer [is with-test]]
            [clojure.java.io :as io]))

(defn input
  [filename]
  (->> (io/resource filename)
       io/reader
       line-seq
       (map #(Integer/parseInt %))))

(defn graph
  [input]
  (let [charging-outlet 0
        device-built-in (+ 3 (apply max input))
        available-joltages (set (conj (set input)
                                      charging-outlet))]
    (assoc (->> available-joltages
                (reduce (fn [g node]
                          (assoc g
                            node (set (filter available-joltages
                                              (range (+ node 1)
                                                     (+ node 4))))))
                        {}))
      device-built-in #{})))

(defn topological-ordering
  "Kahn's algorithm"
  [g]
  (loop [g g, res []]
    (if-let [nodes (->> g (filter (comp empty? second)) (map first) seq)]
      (recur (reduce-kv #(assoc %1 %2 (apply disj %3 nodes)) {} (apply dissoc g nodes))
             (into res nodes))
      res)))

(with-test
  (defn answer-part-1
    [input]
    (->> (graph input)
         topological-ordering
         (partition 2 1)
         (map #(apply - %))
         frequencies
         vals
         (apply *)))
  (is (= 220 (answer-part-1 (input "day-10-example.txt"))))
  (is (= 2176 (answer-part-1 (input "day-10.txt")))))

(defn with-previous
  [pred]
  (let [previous (volatile! nil)]
    (fn [v]
      (let [x @previous]
        (vreset! previous v)
        (if x
          (pred x v)
          (pred v))))))

(with-test
  (defn split-on
    [f coll]
    (lazy-seq
      (when-let [s (seq coll)]
        (let [run (->> (next s)
                       (take-while #(not (f %)))
                       (cons (first s)))]
          (cons run (split-on f (lazy-seq (drop (count run) s))))))))
  (is (= '((0 1 2 3 4 5)) (split-on #{0} (range 6))))
  (is (= '((0 1 2) (3 4) (5)) (split-on #{3 5} (range 6))))
  (is (= '((0) (1) (2) (3) (4) (5)) (split-on (set (range 6)) (range 6)))))

(defn all-prefixed-paths
  [g v]
  (let [leaves (get g (peek v))]
    (if (seq leaves)
      (lazy-seq (mapcat #(all-prefixed-paths g (conj v %))
                        leaves))
      [v])))

(with-test
  (defn answer-part-2
    [input]
    (let [g (graph input)]
      (->> (sort (keys g))
           ;; Divide
           (split-on (comp #(= 3 %)
                           (with-previous
                             (fn
                               ([_] 0)
                               ([previous v] (- v previous))))))
           ;; Fight
           (map #(let [sub-g (select-keys g %)
                       sub-root (apply min %)]
                   (all-prefixed-paths sub-g [sub-root])))
           ;; Conquer
           (map count)
           (reduce *))))
  (is (= 19208 (answer-part-2 (input "day-10-example.txt"))))
  (is (= 18512297918464 (answer-part-2 (input "day-10.txt")))))

(ns cracking-the-coding-interview.trees-and-graphs.exercice-4-dot-7-build-order
  (:require [clojure.string :as str]
            [clojure.test :refer [deftest is]]))

(defn topological-ordering "Kahn's algorithm" [g]
  (loop [g g, res []]
    (if-let [nodes (->> g (filter (comp empty? second)) (map first) seq)]
      (recur (reduce-kv #(assoc %1 %2 (apply disj %3 nodes)) {} (apply dissoc g nodes))
             (into res nodes))
      res)))

(deftest topological-ordering-test
  (is (= [] (topological-ordering {})))
  (is (= [:d :c :b :a] (topological-ordering {:a #{:b}
                                              :b #{:c}
                                              :c #{:d}
                                              :d #{}})))
  (is (= [:e :f :a :b :d :c] (topological-ordering {:a #{:f}
                                                    :b #{:f}
                                                    :c #{:d}
                                                    :d #{:a :b}
                                                    :e #{}
                                                    :f #{}}))))

(defn normalized-input?
  [g]
  (->> (vals g)
       (reduce into)
       (every? (set (keys g)))
       (and (every? set? (vals g)))))

(deftest normalized-input-test
  (is (normalized-input? {}))
  (is (normalized-input? {:a #{}}))
  (is (normalized-input? {:a #{:a}}))
  (is (false? (normalized-input? {:a #{:a :b}})))
  (is (normalized-input? {:a #{:a :b} :b #{}})))

(defn build-order [g]
  (assert (normalized-input? g) "Not normalized input: all nodes
  should be keys.")
  (loop [g g, res []]
    (let [nodes (->> g (filter (comp empty? second)) (map first) seq)]
      (if nodes 
        (recur (reduce-kv #(assoc %1 %2 (apply disj %3 nodes)) {} (apply dissoc g nodes))
               (into res nodes))
        (do (assert (empty? g) "Impossible ordering: a cycle exists.")
            res)))))

(deftest build-order-test
  (is (= [] (build-order {})))
  (is (= [:d :c :b :a] (build-order {:a #{:b}
                                     :b #{:c}
                                     :c #{:d}
                                     :d #{}})))
  (is (= :exception
         (try
           (build-order {:a #{:f}
                         :b #{:f}
                         :c #{:d}
                         :d #{:a :b}
                         :e #{}
                         :f #{:d}})
           (catch AssertionError e
             :exception))))
  (is (= [:e :f :a :b :d :c] (build-order {:a #{:f}
                                           :b #{:f}
                                           :c #{:d}
                                           :d #{:a :b}
                                           :e #{}
                                           :f #{}}))))

(def response build-order)

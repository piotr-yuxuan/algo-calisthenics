(ns advent-of-code-2020.day-11
  (:require [clojure.java.io :as io]
            [clojure.test :refer [is with-test]]))

(defn adjacent-positions
  [vvs [i j]]
  (remove #{[i j]} (for [x (filter (set (range (count vvs))) (range (dec i) (inc (inc i)))) y (filter (set (range (count (get vvs i)))) (range (dec j) (inc (inc j))))] [x y])))

(defn positions-by-type
  [vvs positions]
  (->> positions
       (map #(get-in vvs %))
       frequencies))

(defn positions
  [vvs]
  (let [js (map count vvs)]
    (for [i (range (count vvs))
          j (range (nth js i))]
      [i j])))

(defn next-position-type
  [adjacent-position-types current-type]
  (cond (and (= current-type \L)
             (zero? (get adjacent-position-types \# 0)))
        \#

        (and (= current-type \#)
             (<= 4 (get adjacent-position-types \# 0)))
        \L

        :else
        current-type))

(defn with-previous
  [pred]
  (let [previous (volatile! nil)]
    (fn [v]
      (let [x @previous]
        (vreset! previous v)
        (if x
          (pred x v)
          (pred v))))))

(defn next-seating-state
  [vvs seating-rule position-strategy]
  (reduce (fn [acc position]
            (assoc-in acc position
              (seating-rule
                (positions-by-type vvs
                                   (position-strategy vvs position))
                (get-in vvs position))))
          vvs
          (positions vvs)))

(defn vvs
  [filename]
  (->> (io/resource filename)
       io/reader
       line-seq
       (mapv vec)))

(with-test
  (defn answer-part-1
    [filename]
    (->> (vvs filename)
         (iterate #(next-seating-state %
                                       next-position-type
                                       adjacent-positions))
         (drop-while (with-previous
                       (fn
                         ([_] true)
                         ([previous v] (not= previous v)))))
         first
         (mapcat identity)
         (filter #{\#})
         count))
  (is (= 37 (answer-part-1 "day-11-example.txt")))
  ;; Slow 😕 "Elapsed time: 41141.74475 msecs"
  (is (= 2441 (time (answer-part-1 "day-11.txt")))))

(declare memoized-seen-in-direction)

(defn first-position-in-direction
  [vvs [i j] i+ j+]
  (let [i-range (set (range (count vvs)))
        j-range (set (range (count (get vvs i))))
        [next-i next-j :as position] [(i+ i) (j+ j)]]
    (cond (not (and (i-range next-i)
                    (j-range next-j)))
          nil

          (contains? #{\L \#} (get-in vvs position)) position

          :else
          (memoized-seen-in-direction vvs position i+ j+))))

(def memoized-seen-in-direction
  (memoize first-position-in-direction))

(defn seen-positions
  [vvs position]
  (remove nil?
          [(memoized-seen-in-direction vvs position dec dec)
           (memoized-seen-in-direction vvs position dec identity)
           (memoized-seen-in-direction vvs position dec inc)

           (memoized-seen-in-direction vvs position identity dec)
           (memoized-seen-in-direction vvs position identity inc)

           (memoized-seen-in-direction vvs position inc dec)
           (memoized-seen-in-direction vvs position inc identity)
           (memoized-seen-in-direction vvs position inc inc)]))

(defn relaxed-next-position-type
  [adjacent-position-types current-type]
  (cond (and (= current-type \L)
             (zero? (get adjacent-position-types \# 0)))
        \#

        (and (= current-type \#)
             (<= 5 (get adjacent-position-types \# 0)))
        \L

        :else
        current-type))

(with-test
  (defn answer-part-2
    [filename]
    (->> (vvs filename)
         (iterate #(next-seating-state %
                                       relaxed-next-position-type
                                       seen-positions))
         (drop-while (with-previous
                       (fn
                         ([_] true)
                         ([previous v] (not= previous v)))))
         first
         (mapcat identity)
         (filter #{\#})
         count))
  (is (= 26 (answer-part-2 "day-11-example.txt")))
  ;; Really slow 😕 "Elapsed time: 154067.562592 msecs"
  (is (= 2190 (answer-part-2 "day-11.txt"))))

(ns advent-of-code-2020.day-13
  (:require [clojure.java.io :as io]
            [clojure.test :refer [is with-test]]
            [instaparse.core :as insta]
            [malli.core :as m]
            [malli.transform :as transform]))

(def parser
  (insta/parser
    (slurp (io/resource "day-13-grammar.txt"))))

(defn format-input
  [[[_ timestamp] [_ & coaches]]]
  {:timestamp timestamp
   :coaches coaches})

(def Input
  [:map
   [:timestamp int?]
   [:coaches [:vector [:or int? [:= "x"]]]]])

(def decode
  (m/decoder Input (transform/string-transformer)))

(def input
  (->> (io/resource "day-13.txt")
       slurp
       (insta/parse parser)
       format-input
       decode))

(def answer-part-1
  (->> input
       :coaches
       (filter int?)
       (map (juxt #(- % (mod (:timestamp input) %)) identity))
       (sort-by first)
       first
       (apply *)))

(defn greatest-common-divisor [a b]
  (if (zero? b) a (recur b (mod a b))))

(defn extended-euclid-algorithm
  [a b]
  (let [[[old-r r] [old-s s]] (loop [[old-r r] [a b]
                                     [old-s s] [1 0]]
                                (if (zero? r)
                                  [[old-r r] [old-s s]]
                                  (let [quotient (/ old-r r)]
                                    (recur [r (- old-r (* quotient r))]
                                           [s (- old-s (* quotient s))]))))
        bezout-t (if (zero? b) 0 (quot (- old-r (* old-s a)) b))]
    {:bezout-coefficients [old-s bezout-t]
     :greatest-common-divisor old-r}))

(greatest-common-divisor 13 67)
(extended-euclid-algorithm 13 67)

(defn least-common-multiple
  [& xs]
  (reduce (fn [a b] (/ (* a b) (greatest-common-divisor a b))) xs))

(->> input
     :coaches
     (map-indexed vector)
     (filter (comp int? second))
     (map #(zipmap [:div-rest :modulo] %)))

(defn brute-solve-two-inequation-system
  [xrm xsn]
  (let [xrm [0 17]
        xsn [7 41]
        [r m] xrm
        [s n] xsn]
    (assert (zero? (mod (- s r) (greatest-common-divisor m n))) "Impossible to satisfy")
    (map (fn* [] (+ (least-common-multiple m n))) (range))
    (some #(fn [])))
  )

(defn modular-multiplicative-inverse
  [a modulo])

()

(mod 663 17)
(mod 663 41)

(greatest-common-divisor 17 41)

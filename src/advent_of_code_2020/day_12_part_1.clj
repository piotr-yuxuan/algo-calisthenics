(ns advent-of-code-2020.day-12-part-1
  (:require [clojure.java.io :as io]
            [clojure.test :refer [is with-test]]
            [instaparse.core :as insta]
            [malli.core :as m]
            [malli.transform :as transform]))

(def parser
  (insta/parser
    (slurp (io/resource "day-12-grammar.txt"))))

(def Entry
  [:map
   [:action [:enum :N :S :E :W :F :L :R]]
   [:value int?]])

(def move-boat
  {:N #(update %1 :y + %2)
   :S #(update %1 :y - %2)
   :E #(update %1 :x + %2)
   :W #(update %1 :x - %2)})

(def cardinal-points
  ;; Trigonometric natural orientation
  [:N :W :S :E])

(with-test
  (defn turn
    [{:keys [orientation] :as state} value]
    (->> (cycle cardinal-points)
         (drop-while (complement #{orientation}))
         (drop (int (mod (/ value 90) (count cardinal-points))))
         first
         (assoc state :orientation)))
  (is (= {:orientation :W} (turn {:orientation :N} 90)))
  (is (= {:orientation :N} (turn {:orientation :W} -90)))
  (is (= {:orientation :N} (turn {:orientation :S} 180)))
  (is (= {:orientation :W} (turn {:orientation :E} -180)))
  (is (= {:orientation :E} (turn {:orientation :N} 270)))
  (is (= {:orientation :N} (turn {:orientation :W} -90))))

(defn next-state
  [{:keys [orientation] :as state} {:keys [action value]}]
  (cond (= action :F) ((move-boat orientation) state value)
        (= action :L) (turn state value)
        (= action :R) (turn state (- value))
        :else ((move-boat action) state value)))

(defn input
  [filename]
  (->> (io/resource filename)
       io/reader
       line-seq
       (map (comp (m/decoder Entry (transform/string-transformer))
                  #(update % :action keyword)
                  #(into {} %)
                  #(insta/parse parser %)))))

(with-test
  (defn answer
    [input]
    (let [{:keys [x y]} (reduce next-state
                                {:orientation :E, :x 0, :y 0}
                                input)]
      (+ (Math/abs (long x))
         (Math/abs (long y)))))
  (is (= 25 (answer (input "day-12-example.txt"))))
  (is (= 420 (answer (input "day-12.txt")))))

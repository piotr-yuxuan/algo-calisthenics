(ns advent-of-code-2020.day-12-part-2
  (:require [clojure.test :refer [is with-test]]
            [clojure.java.io :as io]
            [instaparse.core :as insta]
            [malli.transform :as transform]
            [malli.core :as m]))

(def parser
  (insta/parser
    (slurp (io/resource "day-12-grammar.txt"))))

(def Entry
  [:map
   [:action [:enum :N :S :E :W :F :L :R]]
   [:value int?]])

(defn move-boat
  [{:keys [orientation] :as state} value]
  (case orientation
    :N (update state :boat/y + value)
    :S (update state :boat/y - value)
    :E (update state :boat/x + value)
    :W (update state :boat/x - value)))

(defn move-waypoint
  [state action value]
  (case action
    :N (update state :waypoint/y + value)
    :S (update state :waypoint/y - value)
    :E (update state :waypoint/x + value)
    :W (update state :waypoint/x - value)))

(defn next-state
  [state {:keys [action value]}]
  (cond (= action :F) (move-boat state value)
        (= action :L) (rotate-waypoint state value)
        (= action :R) (rotate-waypoint state (- value))
        :else (move-waypoint state action value)))

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
    (let [{:keys [boat/x boat/y]} (reduce next-state
                                          {:orientation :E
                                           :boat/x 0
                                           :boat/y 0
                                           ;; The waypoint is relative to the ship
                                           :waypoint/x 10
                                           :waypoint/y 1}
                                          input)]
      (+ (Math/abs (long x))
         (Math/abs (long y)))))
  (is (= 25 (answer (input "day-12-example.txt"))))
  (is (= 420 (answer (input "day-12.txt")))))

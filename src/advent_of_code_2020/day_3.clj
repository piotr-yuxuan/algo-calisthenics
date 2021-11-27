(ns advent-of-code-2020.day-3
  (:require [clojure.java.io :as io]
            [clojure.test :refer [is with-test]]))

(with-test
  (defn answer
    []
    (->> (io/resource "day-3.txt")
         (io/reader)
         line-seq
         (reduce (fn [{:keys [trees-seen index]} line]
                   {:trees-seen (if (= \# (get line index))
                                  (inc trees-seen)
                                  trees-seen)
                    :index (mod (+ 3 index) (count line))})
                 {:trees-seen 0
                  :index 0})
         :trees-seen))
  (is (= 242 (answer))))

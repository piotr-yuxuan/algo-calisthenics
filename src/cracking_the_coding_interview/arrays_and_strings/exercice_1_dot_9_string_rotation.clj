(ns cracking-the-coding-interview.arrays-and-strings.exercice-1-dot-9-string-rotation
  (:require [clojure.test :refer [deftest is]]
            [clojure.string :as str]))

(defonce call-me-once
  (atom 0))

(defn is-sub-string
  [s sub]
  (swap! call-me-once inc)
  (assert (= 1 @call-me-once))
  (str/includes? s sub))

(defn string-rotation
  [s1 s2]
  (reset! call-me-once 0)
  (and (= (count s1) (count s2))
       (is-sub-string (str s2 s2) s1)))

(deftest string-rotation-test
  (is (not (string-rotation "waterbottle" "erbottlewa")))
  (is (not (string-rotation "waterbottl" "erbottlewat")))
  (is (string-rotation "waterbottle" "erbottlewat")))

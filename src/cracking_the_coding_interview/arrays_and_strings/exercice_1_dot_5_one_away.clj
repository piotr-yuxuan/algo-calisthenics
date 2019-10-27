(ns cracking-the-coding-interview.arrays-and-strings.exercice-1-dot-5-one-away
  (:require [clojure.test :refer [deftest is]]))

(defn one-away
  ([a b]
   (cond (< (inc (count b)) (count a)) #(one-away b a)
         (< (inc (count a)) (count b)) false
         :default #(one-away a b false)))
  ([[a1 & a] [b1 & b] edit-seen?]
   (cond (= nil a1 b1) true
         (= a1 b1) #(one-away a b edit-seen?)
         edit-seen? false
         (= (first a) b1) #(one-away (rest a) b true)
         :default #(one-away a b true))))

(def response #(trampoline one-away %1 %2))

(deftest response-test
  (is (response "pale" "ple"))
  (is (response "pales" "pale"))
  (is (response "pale" "bale"))
  (is (not (response "pale" "bales")))
  (is (not (response "pale" "bae"))))

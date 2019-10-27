(ns cracking-the-coding-interview.arrays-and-strings.exercice-1-dot-4-palindrome-permutation
  (:require [clojure.test :refer [deftest is]]
            [clojure.string :as str]))

(defn palindrome-permutation
  [[i & s] odd-seen?]
  (cond (nil? i) (<= (count odd-seen?) 1)
        (= \space i) #(palindrome-permutation s odd-seen?)
        (odd-seen? i) #(palindrome-permutation s (disj! odd-seen? i))
        :default #(palindrome-permutation s (conj! odd-seen? i))))

(def response #(trampoline palindrome-permutation % (transient #{})))

(deftest response-test
  (is (not (response "azfe   a")))
  (is (response "aze   a z"))
  (is (response "zazea")))

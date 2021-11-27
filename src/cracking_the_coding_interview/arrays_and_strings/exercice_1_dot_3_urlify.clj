(ns cracking-the-coding-interview.arrays-and-strings.exercice-1-dot-3-urlify
  (:require [clojure.string :as str]
            [clojure.test :refer [deftest is]]))

(defn urlify
  [s l]
  (let [builder (StringBuilder. ^String s)]
    (loop [i 0]
      (when (= \space (.charAt builder i))
        (doto builder
          (.deleteCharAt i)
          (.insert i "%20")))
      (if (= i l)
        (.toString builder)
        (recur (inc i))))))

(def response urlify)

(deftest response-test
  (let [actual "Mr John Smith"
        expected "Mr%20John%20Smith"]
    (is (= (response actual (count actual))
           expected))))

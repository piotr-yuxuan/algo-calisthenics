(ns cracking-the-coding-interview.arrays-and-strings.exercice-1-dot-6-string-compression
  (:require [clojure.test :refer [deftest is]]))

(defn insert-count!
  [^StringBuilder string-builder ^Integer actual-pointer current-count]
  (.insert string-builder actual-pointer (str current-count)))

(defn string-compression-fn
  [input-length ^StringBuilder string-builder]
  (fn string-compression
    [{:keys [expected-pointer current-count actual-pointer] :as args}]
    (cond ;; Termination tests
          (<= input-length actual-pointer) nil

          (= (.length string-builder) actual-pointer)
          (str (doto string-builder (insert-count! actual-pointer current-count)))

          ;; Tests to find similar letters or move forward
          (= expected-pointer actual-pointer)
          #(string-compression (update args :actual-pointer inc))

          (= (.charAt string-builder expected-pointer) (.charAt string-builder actual-pointer))
          (do (.deleteCharAt string-builder actual-pointer)
              #(string-compression (update args :current-count inc)))

          ;; End of a streak
          :default
          (do (insert-count! string-builder actual-pointer current-count)
              (let [new-expected-pointer (inc actual-pointer)]
                #(string-compression {:expected-pointer new-expected-pointer
                                      :actual-pointer (inc new-expected-pointer)
                                      :current-count 1}))))))

(defn response
  [^String input]
  (-> (string-compression-fn (.length input) (StringBuilder. input))
      (trampoline {:expected-pointer 0 :actual-pointer 0 :current-count 1})
      (or input)))

(deftest response-test
  (is (= "a8" (response "aaaaaaaa")))
  (is (= "aac" (response "aac")))
  (is (= "a3c1" (response "aaac")))
  (is (= "acc" (response "acc")))
  (is (= "a1c3" (response "accc")))
  (is (= "a2c2" (response "aacc")))
  (is (= "aabbc" (response "aabbc")))
  (is (= "a2b1c5a3" (response "aabcccccaaa"))))

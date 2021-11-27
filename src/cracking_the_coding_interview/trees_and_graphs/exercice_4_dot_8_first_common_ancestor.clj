(ns cracking-the-coding-interview.trees-and-graphs.exercice-4-dot-8-first-common-ancestor
  (:require [clojure.string :as str]
            [clojure.test :refer [deftest is]]))

(def tree-ancestors #(apply merge (for [[k vs] % v vs] {v k})))

(deftest tree-ancestors-test
  (let [t {:a #{:b}, :c #{:d :e}}
        ancestor (tree-ancestors t)]
    (is (= :a (ancestor :b)))
    (is (= :c (ancestor :d))) 
    (is (= :c (ancestor :e)))
    (is (nil? (ancestor :a)))))

(defn first-common-ancestor-fn
  [t]
  (let [ancestor (tree-ancestors t)]
    (fn first-common-ancestor [left right common-ancestor?]
      (cond (= left right) left
            (common-ancestor? right) right
            (common-ancestor? left) left
            (not (and left right)) nil
            :default #(first-common-ancestor (ancestor left)
                                             (ancestor right)
                                             (conj common-ancestor? left right))))))

(defn response
  [t left right]
  (trampoline (first-common-ancestor-fn t) left right #{}))

(deftest first-common-ancestor-test
  (let [t {:a #{:b :c}
           :b #{:d :e}
           :c #{:f :g}
           :d #{:h :i}
           :e #{:j :k}
           :f #{:l :m}
           :z #{:y}}]
    (is (= :a (response t :a :a)))
    (is (= :c (response t :g :m)))
    (is (= :a (response t :k :m)))
    (is (nil? (response t :k :z)))))

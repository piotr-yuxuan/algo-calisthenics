(ns cracking-the-coding-interview.trees-and-graphs.exercice-4-dot-6-successor
  (:require [clojure.test :refer [deftest is]]))

(defn tree-traversal
  [traversal tree root]
  (lazy-seq
   (if-let [[left right] (get tree root)]
     (lazy-cat (when (= traversal :traversal/pre-order) (list root))
               (tree-traversal traversal tree left)
               (when (= traversal :traversal/in-order) (list root))
               (tree-traversal traversal tree right)
               (when (= traversal :traversal/post-order) (list root)))
     (list root))))

(deftest tree-traversal-test
  (is (= (range 1 8)
         (let [t {1 [2 5], 2 [3 4], 5 [6 7], :root 1}] (tree-traversal :traversal/pre-order t (:root t)))
         (let [t {2 [1 3], 4 [2 6], 6 [5 7], :root 4}] (tree-traversal :traversal/in-order t (:root t)))
         (let [t {3 [1 2], 6 [4 5], 7 [3 6], :root 7}] (tree-traversal :traversal/post-order t (:root t))))))

(def reverse-graph
  #(apply merge-with clojure.set/union (for [[k vs] % v vs] {v #{k}})))

(defn- successor
  [tree node]
  (let [parent (comp first (reverse-graph (dissoc tree :root)))]
    (if-let [right (last (get tree node))]
      (->> (iterate (comp first tree) right)
           (take-while some?)
           last)
      (->> (iterate parent node)
           (take-while some?)
           (partition 2 1)
           (some (fn [[n p]] (when (= n (first (get tree p))) p)))))))

(deftest successor-test
  (let [t {2 [1 3], 4 [2 6], 6 [5 7], :root 4}]
    (is (= 2 (successor t 1)))
    (is (= 3 (successor t 2)))
    (is (= 4 (successor t 3)))
    (is (= 5 (successor t 4)))
    (is (= 6 (successor t 5)))
    (is (= 7 (successor t 6)))
    (is (not (successor t 7)))))

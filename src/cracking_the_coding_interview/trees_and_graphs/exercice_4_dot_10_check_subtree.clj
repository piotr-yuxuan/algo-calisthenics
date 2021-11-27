(ns cracking-the-coding-interview.trees-and-graphs.exercice-4-dot-10-check-subtree
  (:require [clojure.string :as str]
            [clojure.test :refer [deftest is testing]])
  (:import (clojure.lang PersistentQueue)))

(defn tree-traversal
  [order tree coll]
  (lazy-seq
   (when (seq coll)
     (let [children (->> (peek coll)
                         (get tree)
                         order)
           successors (into (pop coll)
                            children)]
       ;; depth/breadth is different from
       ;; pre-order/in-order/post-order.
       (cons (peek coll)
             (tree-traversal order
                             tree
                             successors))))))

(def depth<-first #(tree-traversal identity %1 (list %2)))
(def depth->first #(tree-traversal reverse %1 (list %2)))
(def breadth<-first #(tree-traversal reverse %1 (conj (PersistentQueue/EMPTY) %2)))
(def breadth->first #(tree-traversal identity %1 (conj (PersistentQueue/EMPTY) %2)))

(deftest tree-traversal-test
  (let [t {:root 0,
           0 '(1 2)
           1 '(3 4)
           2 '(5 6)
           3 '(7 8)
           4 '(9 10)
           5 '(11 12)
           6 '(13 14)}]
    (is (= (breadth->first t 0) (list 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14)))
    (is (= (breadth<-first t 0) (list 0 2 1 6 5 4 3 14 13 12 11 10 9 8 7)))
    (is (= (depth<-first t 0)   (list 0 2 6 14 13 5 12 11 1 4 10 9 3 8 7)))
    (is (= (depth->first t 0)   (list 0 1 3 7 8 4 9 10 2 5 11 12 6 13 14)))))

(defn check-subtree [t1 t2]
  (let [traversal-t1 (depth->first t1 (:root t1))
        traversal-t2 (depth->first t2 (:root t2))]
    (->> traversal-t1
         (map-indexed vector)
         (some (fn [[index r]]
                 (-> index
                     (drop traversal-t1)
                     (= traversal-t2))))
         boolean)))

(deftest check-subtree-test
  (testing "two identical subtrees"
    (let [t1 {0 '(1 2), 1 '(3 4), 4 '(9 10), 13 '(15 16), 6 '(13 14), 3 '(7 8), :root 0, 2 '(5 6), 5 '(11 12), 14 '(17 18)}
          t2 {:root 6, 6 '(13 14), 13 '(15 16), 14 '(17 18)}]
      (is (true? (check-subtree t1 t2)))))
  (testing "t2 in t1 but with deeper leaves"
    (let [t1 {0 '(1 2), 1 '(3 4), 4 '(9 10), 13 '(15 16), 6 '(13 14), 3 '(7 8), :root 0, 2 '(5 6), 5 '(11 12), 14 '(17 18), 17 '(19 20)}
          t2 {:root 6, 6 '(13 14), 13 '(15 16), 14 '(17 18)}]
      (is (false? (check-subtree t1 t2)))))
  (testing "different subtrees"
    (let [t1 {0 '(1 2), 1 '(3 4), 4 '(9 10), 13 '(15 16), 6 '(13 14), 3 '(7 8), :root 0, 2 '(5 6), 5 '(11 12), 14 '(17 18)}
          t2 {:root 6, 6 '(13 :lol), 13 '(15 16), 14 '(17 18)}]
      (is (false? (check-subtree t1 t2))))))

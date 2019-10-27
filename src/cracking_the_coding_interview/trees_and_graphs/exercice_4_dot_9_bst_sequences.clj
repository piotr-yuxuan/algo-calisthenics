(ns cracking-the-coding-interview.trees-and-graphs.exercice-4-dot-9-bst-sequences
  (:require [clojure.test :refer [deftest is]]
            [clojure.string :as str]))

(defn shape [t]
  (let [[left right] (get t (:root t))
        [sub-left sub-right] (get t (or left right))]
    (->> (vector (:root t)
                 left
                 right
                 sub-left
                 sub-right)
         (map boolean)
         vec)))

(def arrays
  {[true true true false false] (fn [t] (let [[left right] (get t (:root t))]
                                          (hash-set [(:root t) right left]
                                                    [(:root t) left right])))
   [true false true false true] (fn [t] (let [[_ right] (get t (:root t))
                                              [_ sub-right] (get t right)]
                                          (hash-set [(:root t) right sub-right])))
   [true false true true false] (fn [t] (let [[_ right] (get t (:root t))
                                              [sub-left _] (get t right)]
                                          (hash-set [(:root t) right sub-left])))
   [true true false true false] (fn [t] (let [[left _] (get t (:root t))
                                              [sub-left _] (get t left)]
                                          (hash-set [(:root t) left sub-left])))
   [true true false false true] (fn [t] (let [[left _] (get t (:root t))
                                              [_ sub-right] (get t left)]
                                          (hash-set [(:root t) left sub-right])))})

(defn bst-sequences [t]
  ((arrays (shape t)) t))

(deftest bst-sequences-test
  (is (= (bst-sequences {:root 2, 2 [1 3]})
         #{[2 1 3], [2 3 1]}))
  (is (= (bst-sequences {:root 1, 1 [nil 2], 2 [nil 3]})
         #{[1 2 3]}))
  (is (= (bst-sequences {:root 1, 1 [nil 3], 3 [2 nil]})
         #{[1 3 2]}))
  (is (= (bst-sequences {:root 3, 3 [2 nil], 2 [1 nil]})
         #{[3 2 1]}))
  (is (= (bst-sequences {:root 3, 3 [1 nil], 1 [2 nil]})
         #{[3 1 2]})))

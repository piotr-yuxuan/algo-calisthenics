(ns cracking-the-coding-interview.trees-and-graphs.exercice-4-dot-4-check-balanced
  (:require [clojure.test :refer [deftest is]]
            [clojure.string :as str]))

(defn balanced-height
  "Return height, or false if unbalanced"
  [t node]
  (let [[left right] (get t node)
        left-height (if left
                      (balanced-height t left)
                      0)
        right-height (cond (false? left-height) false
                           right (balanced-height t right)
                           :default 0)]
    (and right-height
         (< (Math/abs (- left-height right-height)) 2)
         (if node (inc (max left-height right-height)) 0))))

(def check-balance
  (comp boolean balanced-height))

(deftest balance-test
  (let [t {:root nil}]
    (is (= 0 (balanced-height t (:root t))))
    (is (check-balance t (:root t))))
  (let [t {:root 0
           0 '(nil nil)}]
    (is (= 1 (balanced-height t (:root t))))
    (is (check-balance t (:root t))))
  (let [t {:root 0
           0 '(nil 1)
           1 '(nil nil)}]
    (is (= 2 (balanced-height t (:root t))))
    (is (check-balance t (:root t))))
  (let [t {:root 1
           1 '(0 2)
           0 '(nil nil)
           2 '(nil nil)}]
    (is (= 2 (balanced-height t (:root t))))
    (is (check-balance t (:root t))))
  (let [t {:root 1
           1 '(0 2)
           0 '(nil nil)
           2 '(nil 3)
           3 '(nil nil)}]
    (is (= 3 (balanced-height t (:root t))))
    (is (check-balance t (:root t))))
  (let [t {:root 1
           1 '(0 2)
           0 '(nil nil)
           2 '(nil 3)
           3 '(nil 4)
           4 '(nil nil)}]
    (is (false? (balanced-height t (:root t))))
    (is (not (check-balance t (:root t))))))

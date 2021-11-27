(ns cracking-the-coding-interview.trees-and-graphs.exercice-4-dot-5-validate-bst
  (:require [clojure.string :as str]
            [clojure.test :refer [deftest is]]))

(declare bst-bounds)

(defn- leaves-pred
  [t node]
  (let [[left right] (get t node)]
    (->> [left node right]
         (remove nil?)
         (apply <))))

(defn- subtrees-pred
  [t node left right]
  (let [[right-min _] (bst-bounds t right)
        [_ left-max] (bst-bounds t left)]
    (and  (some? left-max)
          (some? right-min)
          (< left-max node right-min))))

(defn- bst-bounds
  [t node]
  (let [[left right] (get t node)
        nodes (->> [left node right] (remove nil?))]
    (cond (= [nil nil] [left right])
          [node node]

          (and (leaves-pred t node) (subtrees-pred t node left right))
          (vector (apply min nodes) (apply max nodes)))))

(def validate-bst (comp boolean bst-bounds))

(deftest validate-bst-test
  (let [t {:root 6
           6 '(3 9)}]
    (is (true? (validate-bst t (get t :root)))))
  (let [t {:root 6
           6 '(5 3)}]
    (is (false? (validate-bst t (get t :root)))))
  (let [t {:root 6
           6 '(9 3)}]
    (is (false? (validate-bst t (get t :root)))))
  (let [t {:root 6
           6 '(3 9)
           9 '(5 10)}]
    (is (false? (validate-bst t (get t :root)))))
  (let [t {:root 6
           6 '(3 9)
           9 '(7 10)}]
    (is (true? (validate-bst t (get t :root)))))
  (let [t {:root 6
           6 '(3 9)
           3 '(2 4)
           9 '(5 10)}]
    (is (false? (validate-bst t (get t :root)))))
  (let [t {:root 6
           6 '(3 9)
           3 '(2 8)
           9 '(7 10)}]
    (is (false? (validate-bst t (get t :root)))))
  (let [t {:root 6
           6 '(3 9)
           3 '(2 4)
           9 '(7 10)}]
    (is (true? (validate-bst t (get t :root))))))

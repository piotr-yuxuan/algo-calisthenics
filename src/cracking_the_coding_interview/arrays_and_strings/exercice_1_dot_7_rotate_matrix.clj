(ns cracking-the-coding-interview.arrays-and-strings.exercice-1-dot-7-rotate-matrix
  (:require [clojure.test :refer [deftest is testing]]))

(defn rotate-coordinates
  [side [x y]]
  (vector (- (dec side) y)
          x))

(deftest rotate-coordinate-test
  (testing "side of 1"
    (is (= (rotate-coordinates 1 [0 0]) [0 0])))
  (testing "side of 2"
    (is (= (rotate-coordinates 2 [0 0]) [1 0]))
    (is (= (rotate-coordinates 2 [0 1]) [0 0]))
    (is (= (rotate-coordinates 2 [1 0]) [1 1])))
  (testing "side of 3"
    (is (= (rotate-coordinates 3 [0 0]) [2 0]))
    (is (= (rotate-coordinates 3 [0 1]) [1 0]))
    (is (= (rotate-coordinates 3 [0 2]) [0 0]))
    (is (= (rotate-coordinates 3 [1 0]) [2 1]))
    (is (= (rotate-coordinates 3 [2 0]) [2 2]))
    (is (= (rotate-coordinates 3 [1 1]) [1 1]))))

(defn rotate-matrix
  [matrix]
  (let [side (count matrix)]
    (reduce (fn [rotated-matrix coordinates]
              (assoc-in rotated-matrix
                        (rotate-coordinates side coordinates)
                        (get-in matrix coordinates)))
            matrix
            (for [x (range side) y (range side)] [x y]))))

(defn- random-matrix
  [side]
  (vec (repeatedly side (fn [] (vec (repeatedly side #(rand-int 42)))))))

(deftest rotate-matrix-test
  (testing "four rotations equate identity"
    (let [rotate-ident #(nth (iterate rotate-matrix %) 4)]
      (doseq [side (range 5)]
        (let [matrix (random-matrix side)]
          (is (= matrix (rotate-ident matrix)))))))
  (testing "side 1"
    (is (= (rotate-matrix [[1]]) [[1]])))
  (testing "side 2"
    (is (= (rotate-matrix [[1 2]
                           [4 3]])
           [[2 3]
            [1 4]])))
  (testing "side 3"
    (is (= (rotate-matrix [[1 10 2]
                           [40 5 20]
                           [4 30 3]])
           [[2 20 3]
            [10 5 30]
            [1 40 4]]))))

(defn matrix-in-place-swap!
  "https://en.wikipedia.org/wiki/XOR_swap_algorithm"
  [matrix! [x1 y1] [x2 y2]]
  (assoc! (get matrix! x1) y1 (bit-xor (get-in matrix! [x1 y1]) (get-in matrix! [x2 y2])))
  (assoc! (get matrix! x2) y2 (bit-xor (get-in matrix! [x2 y2]) (get-in matrix! [x1 y1])))
  (assoc! (get matrix! x1) y1 (bit-xor (get-in matrix! [x1 y1]) (get-in matrix! [x2 y2]))))

(defn- empty-matrix
  [side]
  (vec (repeatedly side (fn [] (vec (repeatedly side (fn [] 0)))))))

(defn- matrix!->persistent-copy
  [matrix!]
  (let [side (count matrix!)]
    (reduce #(assoc-in %1 %2 (get-in matrix! %2))
            (empty-matrix side)
            (for [x (range side) y (range side)] [x y]))))

(defn- empty-matrix!
  [side]
  (transient (vec (repeatedly side (fn [] (transient (vec (repeatedly side (fn [] 0)))))))))

(defn- shuffle-no-fix-point
  [coll]
  (-> (count coll)
      dec
      rand-int
      inc
      (drop (cycle coll))))

(deftest matrix-in-place-swap!-test
  (doseq [side (range 2 5)]
    (let [coordinates (for [x (range side) y (range side)] [x y])]
      (doseq [[[x y :as coordinates] new-coordinates] (zipmap coordinates (shuffle-no-fix-point coordinates))]
        (let [matrix! (empty-matrix! side)]
          (assoc! matrix! x (assoc! (get matrix! x) y 1))
          (matrix-in-place-swap! matrix! coordinates new-coordinates)
          (let [actual (matrix!->persistent-copy matrix!)]
            (is (= actual (assoc-in (empty-matrix side) new-coordinates 1)))))))))

(defn- possible-indices
  "Compute rotation indices given the `side` of the matrix and the
  `offset` of the ring. The latter parameter, when `0`, points the all
  the outer sites of the matrix. The highest index value refers to the
  innermost ring of the matrix."
  [side offset]
  (-> side
      dec
      (- (* 2 offset))
      range))

(defn- ring-rotations
  "For a given ring of the matrix, list all the rotation cycles. The
  rotations first contains the cycle for the left-hand top corners,
  then their 'right-side neighbour', and so on until all rotation
  indices are exhausted."
  [side ring]
  (map (fn [index]
         (if (= ring (/ (dec side) 2))
           (vector [ring ring])
           (vector [ring (+ ring index)]
                   [(+ ring index) (- (dec side) ring)]
                   [(- (dec side) ring) (- (dec side) ring index)]
                   [(- (dec side) ring index) ring])))
       (possible-indices side ring)))

(defn- all-ring-rotations
  "`side` is the side of the matrix. This functions returns all the
  cycle of rotation for all the matrix sites. Each site appear once
  and only once in the rotation cycles."
  [side]
  (mapcat (fn [ring]
            (ring-rotations side ring))
          (range (/ side 2))))

(defn rotate-matrix!
  [matrix!]
  (let [side (count matrix!)]
    (doseq [rotation (all-ring-rotations side)
            i (range (dec (count rotation)))]
      (matrix-in-place-swap! matrix! (get rotation i) (get rotation (inc i))))))

(defn- random-matrix!
  [side]
  (transient (vec (repeatedly side (fn [] (transient (vec (repeatedly side #(rand-int 42)))))))))

(deftest rotate-matrix!-test
  (testing "four rotations equate identity"
    (doseq [side (range 5)]
      (let [matrix! (random-matrix! side)
            matrix-copy (matrix!->persistent-copy matrix!)]
        (dotimes [_ 4] (rotate-matrix! matrix!))
        (is (= matrix-copy (matrix!->persistent-copy matrix!))))))
  (testing "side 1"
    (let [matrix! (transient [(transient [1])])]
      (rotate-matrix! matrix!)
      (is (= (matrix!->persistent-copy matrix!) [[1]]))))
  (testing "side 2"
    (let [matrix! (transient [(transient [1 2])
                              (transient [4 3])])]
      (rotate-matrix! matrix!)
      (is (= (matrix!->persistent-copy matrix!)
             [[2 3]
              [1 4]]))))
  (testing "side 3"
    (let [matrix! (transient [(transient [1 10 2])
                              (transient [40 5 20])
                              (transient [4 30 3])])]
      (rotate-matrix! matrix!)
      (is (= (matrix!->persistent-copy matrix!)
             [[2 20 3]
              [10 5 30]
              [1 40 4]]))))
  (testing "mutable version behaves as previous immutable one"
    (doseq [side (range 5)]
      (dotimes [_ 3]
        (let [matrix! (random-matrix! side)
              matrix-copy (matrix!->persistent-copy matrix!)]
          (rotate-matrix! matrix!)
          (is (= (rotate-matrix matrix-copy)
                 (matrix!->persistent-copy matrix!))))))))

(def response rotate-matrix)

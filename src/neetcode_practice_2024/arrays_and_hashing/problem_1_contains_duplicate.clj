(ns neetcode-practice-2024.arrays-and-hashing.problem-1-contains-duplicate)

(defn merge-sort
  ([l] (merge-sort identity l))
  ([k l]
   (letfn [(merge-lr [left right]
             (persistent!
              (loop [left left
                     right right
                     merged (transient [])]
                (cond (empty? left) (reduce conj! merged right)
                      (empty? right) (reduce conj! merged left)

                      (<= (k (first left)) (k (first right)))
                      (recur (next left) right (conj! merged (first left)))
                      :else
                      (recur left (next right) (conj! merged (first right)))))))]
     (if (<= (count l) 1)
       l
       (let [[left right] (split-at (/ (count l) 2) l)] 
         (merge-lr (merge-sort k left)
                   (merge-sort k right)))))))

(defn solution-not-optimal
  ([l] (solution-not-optimal identity l))
  ([k l]
   (->> (merge-sort k l)
        (partition 2 1)
        (every? (partial apply not=)))))

(defn solution
  ([l] (solution (transient #{}) l))
  ([seen? [i & r]]
   (cond (seen? i) false
         (empty? r) true
         (conj! seen? i) (solution seen? r))))

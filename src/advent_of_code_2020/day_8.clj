(ns advent-of-code-2020.day-8
  (:require [clojure.test :refer [is with-test]]
            [clojure.java.io :as io]
            [clojure.string :as str]))

(defn instructions
  [file]
  (->> (line-seq (io/reader (io/resource file)))
       (map (comp #(zipmap [:operation :argument] %)
                  (juxt (comp keyword
                              first)
                        (comp #(Integer/parseInt ^String %)
                              second))
                  #(str/split % #"\s+")))
       ;; Allow direct jumps to instruction, don't rewind every time.
       vec))

(defn execute-instruction
  [instructions {:keys [position] :as state}]
  (let [{:keys [operation argument] :as current-instruction} (nth instructions position)]
    (cond-> state
      :always (assoc :instruction current-instruction)
      (contains? #{:acc} operation) (update :accumulator + argument)
      (contains? #{:jmp} operation) (update :position + argument)
      (contains? #{:nop :acc} operation) (update :position inc)
      :always (update :previous-positions conj position))))

(defn run-program
  [instructions]
  (iterate (partial execute-instruction instructions)
           {:accumulator 0
            :previous-positions #{}
            :position 0
            :instruction nil}))

(with-test
  (defn answer-part-1
    [instructions]
    (->> (run-program instructions)
         (some (fn [{:keys [accumulator previous-positions position]}]
                 (cond (previous-positions position) accumulator)))))
  (is (= 5 (answer-part-1 (instructions "day-8-example.txt"))))
  (is (= 1586 (answer-part-1 (instructions "day-8.txt")))))

(defn terminate-program
  [instructions states]
  (->> states
       (some (fn [{:keys [accumulator previous-positions position]}]
               (cond (previous-positions position) {:reason :infinite-loop
                                                    :accumulator accumulator}
                     (= position (count instructions)) {:reason :last-instruction
                                                        :accumulator accumulator})))))

(with-test
  (defn answer-part-2
    [instructions]
    (let [corrup-indices (->> (map-indexed vector instructions)
                              (filter (comp #{:nop :jmp} :operation second))
                              (map first))]
      (letfn [(possible-repaired-instructions [[i & indices]]
                (when i
                  (lazy-seq (cons (update-in instructions
                                    [i :operation]
                                    {:jmp :nop, :nop :jmp})
                                  (possible-repaired-instructions indices)))))]
        (->> corrup-indices
             possible-repaired-instructions
             (map (comp #(terminate-program instructions %)
                        run-program))
             (some #(when (= (:reason %) :last-instruction) %))))))
  (is (= {:reason :last-instruction, :accumulator 8}
         (answer-part-2 (instructions "day-8-example.txt"))))
  (is (= {:reason :last-instruction, :accumulator 703}
         (answer-part-2 (instructions "day-8.txt")))))

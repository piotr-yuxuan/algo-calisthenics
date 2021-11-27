(ns advent-of-code-2020.day-7
  (:require [clojure.java.io :as io]
            [clojure.test :refer [is with-test]]
            [instaparse.core :as insta]))

(def parser
  (insta/parser
    (slurp (io/resource "day-7-grammar.txt"))))

(with-test
  (def reverse-graph
    #(apply merge-with clojure.set/union (for [[k vs] % v vs] {v #{k}})))
  (is (= (reverse-graph
           {:a #{:b :c}
            :b #{:d :e}
            :c #{:f :g}})
         {:b #{:a}
          :c #{:a}
          :d #{:b}
          :e #{:b}
          :f #{:c}
          :g #{:c}})))

(def graph-entry-no-weight
  (juxt first
        (comp #(into #{} %)
              (partial map last)
              rest)))

(with-test
  (defn transitive-children
    [node g]
    (->> (get g node)
         (map #(transitive-children % g))
         (apply clojure.set/union)
         (clojure.set/union (get g node))))
  (is (= (transitive-children
           :a
           {:a #{:b :c}
            :b #{:d :e}
            :c #{:f :g}})
         #{:b :c :d :e :f :g})))

(with-test
  (defn answer-part-1
    []
    (->> (io/resource "day-7.txt")
         io/reader
         line-seq
         (map #(insta/parse parser %))
         (map graph-entry-no-weight)
         reverse-graph
         (transitive-children [:colour "shiny" "gold"])
         count))
  (is (= (answer-part-1) 155)))

(def graph-entry-weighted
  (juxt first
        (comp #(into {} %)
              (partial map (comp vec
                                 (fn [[_ weight colour]]
                                   [colour (Integer/parseInt weight)])))
              rest)))

(defn children-edge-weight-sum
  [node g]
  (let [weights (get g node)]
    (->> (keys weights)
         (map #(* (get weights %) (children-edge-weight-sum % g)))
         (reduce + (reduce + (vals weights))))))

(with-test
  (defn answer-part-2
    []
    (->> (io/resource "day-7.txt")
         io/reader
         line-seq
         (map #(insta/parse parser %))
         (map graph-entry-weighted)
         (into {})
         (children-edge-weight-sum [:colour "shiny" "gold"])))
  (is (= (answer-part-2) 54803)))

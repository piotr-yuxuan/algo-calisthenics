(ns advent-of-code-2020.day-4
  (:require [clojure.test :refer [is with-test]]
            [clojure.java.io :as io]
            [instaparse.core :as insta]
            [clojure.string :as str]))

(def mandatory-keys
  [:byr :iyr :eyr :hgt :hcl :ecl :pid])

(with-test
  (defn concat-lines-paragraph
    [coll]
    (->> coll
         (partition-by #{""})
         (remove #{'("")})
         (map #(str/join " " %))))
  (is (= ["ecl:gry pid:860033327 eyr:2020 hcl:#fffffd byr:1937 iyr:2017 cid:147 hgt:183cm"
          "iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884 hcl:#cfa07d byr:1929"
          "hcl:#ae17e1 iyr:2013 eyr:2024 ecl:brn pid:760753108 byr:1931 hgt:179cm"
          "hcl:#cfa07d eyr:2025 pid:166559648 iyr:2011 ecl:brn hgt:59in"]
         (concat-lines-paragraph (line-seq (io/reader (io/resource "day-4-example.txt")))))))

(def parser
  (insta/parser
    (slurp (io/resource "day-4-grammar.txt"))))

(with-test
  (defn answer
    []
    (->> (io/resource "day-4.txt")
         (io/reader)
         line-seq
         concat-lines-paragraph
         (map #(insta/parse parser %))
         (remove insta/failure?)
         (map (fn [fields] (->> fields
                                (filter (comp #{:key} first))
                                (map (comp keyword second))
                                set)))
         (filter #(every? % mandatory-keys))
         count))
  (is (= 239 (answer))))

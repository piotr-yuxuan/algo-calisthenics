(ns advent-of-code-2020.day-2
  (:require [clojure.java.io :as io]
            [clojure.test :refer [is with-test]]
            [instaparse.core :as insta]
            [malli.core :as m]
            [malli.transform :as transform]))

(def Entry
  [:map
   [:lowest int?]
   [:highest int?]
   [:letter char?]
   [:password string?]])

(def parser
  (insta/parser
    (slurp (io/resource "day-2-grammar.txt"))))

(with-test
  (defn answer
    []
    (->> (io/resource "day-2.txt")
         io/reader
         line-seq
         (map (comp #(into {} %) #(insta/parse parser %)))
         (map (m/decoder Entry (transform/string-transformer)))
         (map #(update % :letter first)) ;; malli decodes into a string
         (map #(assoc % :letter-frequencies (frequencies (:password %))))
         (filter (fn [{:keys [lowest highest letter letter-frequencies]}]
                   (when-let [actual (get letter-frequencies letter)]
                     (<= lowest actual highest))))
         count))
  (is (= (answer) 580)))



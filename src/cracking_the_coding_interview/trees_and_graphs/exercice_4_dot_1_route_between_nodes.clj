(ns cracking-the-coding-interview.trees-and-graphs.exercice-4-dot-1-route-between-nodes
  (:require [clojure.string :as str]
            [clojure.test :refer [deftest is]]))

(defn route-between-nodes
  ([graph from to]
   (route-between-nodes graph from to (transient #{})))
  ([graph from to seen]
   (cond (contains? seen from) false
         (contains? (get graph from) to) true
         (conj! seen from) (->> from
                                (get graph)
                                (some #(route-between-nodes graph % to seen))
                                boolean))))

(deftest route-between-nodes-test
  (is (not (route-between-nodes {:a #{:b}} :a :c)))
  (is (route-between-nodes {:a #{:b}} :a :b))
  (is (not (route-between-nodes {:a #{:b}} :b :a)))
  (is (not (route-between-nodes {:a #{:b}} :a :a)))
  (is (route-between-nodes {:a #{:a :b}} :a :a))
  (is (route-between-nodes {:a #{:a :b}
                            :b #{:a :c}
                            :c #{:d :e}
                            :e #{:f}
                            :f #{:a :b :c :d :e :f :g}
                            :g #{}}
                           :a
                           :g))
  (is (route-between-nodes {:a #{:b}
                            :b #{:a :c}
                            :c #{:b}}
                           :a :b))
  (is (route-between-nodes {:a #{:b}
                            :b #{:a :c}
                            :c #{:b}}
                           :a :c))
  (is (not (route-between-nodes {:a #{:b}
                                 :b #{:a :c}
                                 :c #{:b}}
                                :a :d))))

(defn route-between-nodes-2
  [graph from to]
  (loop [from from
         reachable (get graph from)
         seen? #{}]
    (cond (contains? reachable to) true
          (seen? from) false
          :default (when-let [new-from (some->> reachable
                                                (remove seen?)
                                                (remove #{from})
                                                seq
                                                rand-nth)]
                     (recur new-from
                            (into reachable (get graph new-from))
                            (conj seen? from))))))

(deftest route-between-nodes-2-test
  (is (not (route-between-nodes-2 {:a #{:b}} :a :c)))
  (is (route-between-nodes-2 {:a #{:b}} :a :b))
  (is (not (route-between-nodes-2 {:a #{:b}} :b :a)))
  (is (not (route-between-nodes-2 {:a #{:b}} :a :a)))
  (is (route-between-nodes-2 {:a #{:a :b}} :a :a))
  (is (route-between-nodes-2 {:a #{:a :b}
                              :b #{:a :c}
                              :c #{:d :e}
                              :e #{:f}
                              :f #{:a :b :c :d :e :f :g}
                              :g #{}}
                             :a
                             :g))
  (is (route-between-nodes-2 {:a #{:b}
                              :b #{:a :c}
                              :c #{:b}}
                             :a :b))
  (is (route-between-nodes-2 {:a #{:b}
                              :b #{:a :c}
                              :c #{:b}}
                             :a :c))
  (is (not (route-between-nodes-2 {:a #{:b}
                                   :b #{:a :c}
                                   :c #{:b}}
                                  :a :d))))

(defn reverse-adjacency-map
  [m]
  (reduce (fn [acc [k vs]]
            (reduce #(update %1 %2 (fnil conj #{}) k)
                    acc
                    vs))
          (empty m)
          m))

(deftest reverse-adjacency-map-test
  (= (reverse-adjacency-map {:a #{1 2}
                             :b #{2 3}})
     {1 #{:a}
      2 #{:a :b}
      3 #{:b}})
  (let [adjacency-map {:a #{1 2}
                       :b #{2 3}}]
    (= (->> adjacency-map
            reverse-adjacency-map
            reverse-adjacency-map)
       adjacency-map)))

(defn route-between-nodes-3
  [graph from to]
  (let [adjacency-> graph
        adjacency<- (reverse-adjacency-map graph)
        node-> from
        node<- to]
    (loop [border-> (get adjacency-> node-> #{})
           reachable-> border->
           border<- (get adjacency<- node<- #{})
           reachable<- border<-
           seen? #{}]
      (cond (some reachable-> border<-) true
            (empty? border<-) false
            (some reachable<- border->) true
            (empty? border->) false
            :default (let [new-border-> (some->> border->
                                                 (mapcat graph)
                                                 (remove seen?)
                                                 (remove border->)
                                                 set)
                           new-border<- (some->> border<-
                                                 (mapcat graph)
                                                 (remove seen?)
                                                 (remove border<-)
                                                 set)]
                       (recur new-border->
                              (into reachable-> new-border->)
                              new-border<-
                              (into reachable<- new-border<-)
                              (reduce into [seen? new-border-> new-border<-])))))))

(deftest route-between-nodes-3-test
  (is (not (route-between-nodes-3 {:a #{:b}} :a :c)))
  (is (route-between-nodes-3 {:a #{:b}} :a :b))
  (is (not (route-between-nodes-3 {:a #{:b}} :b :a)))
  (is (not (route-between-nodes-3 {:a #{:b}} :a :a)))
  (is (route-between-nodes-3 {:a #{:a :b}} :a :a))
  (is (route-between-nodes-3 {:a #{:a :b}
                              :b #{:a :c}
                              :c #{:d :e}
                              :e #{:f}
                              :f #{:a :b :c :d :e :f :g}
                              :g #{}}
                             :a
                             :g))
  (is (route-between-nodes-3 {:a #{:b}
                              :b #{:a :c}
                              :c #{:b}}
                             :a :b))
  (is (route-between-nodes-3 {:a #{:b}
                              :b #{:a :c}
                              :c #{:b}}
                             :a :c))
  (is (not (route-between-nodes-3 {:a #{:b}
                                   :b #{:a :c}
                                   :c #{:b}}
                                  :a :d))))

(def response route-between-nodes-2)

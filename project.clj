(defproject com.github.piotr-yuxuan/algo-calisthenics (-> "./resources/algo-calisthenics.version" slurp .trim)
  :description "Practice playground as well as a reminder of some common, simple, yet powerful algorithms"
  :url "https://github.com/piotr-yuxuan/walter-ci"
  :license {:name "GNU GPL v3+"
            :url "http://www.gnu.org/licenses/gpl-3.0.en.html"
            :distribution :repo}
  :scm {:name "git"
        :url "https://github.com/piotr-yuxuan/algorithms-datastructures"}
  :pom-addition [:developers [:developer
                              [:name "胡雨軒 Петр"]
                              [:url "https://github.com/piotr-yuxuan"]]]
  :github/private? false
  :main advent-of-code-2020.main
  :dependencies [[camel-snake-kebab "0.4.3"]
                 [clj-time "0.15.2"]
                 [instaparse "1.4.14"]
                 [metosin/malli "0.16.1"]
                 [org.clojure/data.csv "1.1.0"]
                 [org.clojure/clojure "1.12.0-alpha12"]]
  :profiles {:github {:github/topics ["kata" "playground" "algorithm" "practice" "code"]
                      :github/private? false}
             :provided {:dependencies []}
             :dev {:global-vars {*warn-on-reflection* true}}
             :uberjar {:aot :all}})

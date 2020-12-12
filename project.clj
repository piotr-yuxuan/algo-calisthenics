(defproject algorithms-datastructures "0.1.0-SNAPSHOT"
  :description "FIXME: write description"
  :url "http://example.com/FIXME"
  :license {:name "GNU GPL v3+"
            :url "http://www.gnu.org/licenses/gpl-3.0.en.html"
            :addendum "GPL_ADDITION.md"}
  :dependencies [[clj-time "0.15.0"]
                 [instaparse "1.4.10"]
                 [metosin/malli "0.2.1"]
                 [org.clojure/clojure "1.10.0"]]
  :target-path "target/%s"
  :profiles {:uberjar {:aot :all}})

package main

import (
	"fmt"
	"net/http"
	"os"
)

func main() {
	data := "ok"
	if err := os.WriteFile("/data/probe", []byte(fmt.Sprint(os.Getuid())), 0o644); err != nil {
		data = "fail"
	}
	http.HandleFunc("/", func(w http.ResponseWriter, _ *http.Request) {
		w.Header().Set("Content-Type", "text/plain")
		fmt.Fprintf(w, "PB-IMG %d\ndata=%s\n", os.Getuid(), data)
	})
	http.HandleFunc("/healthz", func(w http.ResponseWriter, _ *http.Request) { fmt.Fprint(w, "ok\n") })
	if err := http.ListenAndServe(":8080", nil); err != nil {
		fmt.Fprintln(os.Stderr, err)
		os.Exit(1)
	}
}

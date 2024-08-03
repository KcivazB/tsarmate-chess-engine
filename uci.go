package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
	"strings"
)

var tell = mainTell
var trim = strings.TrimSpace
var low = strings.ToLower

func uci(frGUI chan string, myTell func(text ...string)) {
	tell("info string Hello from uci")
	fromEng, toEng := engine()
	quit := false
	cmd := ""
	words := []string{}
	bm := ""
	for !quit {
		select {
		case cmd = <-frGUI:
			words = strings.Split(cmd, " ") // Get the words from the GUI
		case bm = <-fromEng:
			// Get the best move from the engine
			handleBestMove(bm) //Handle the best move
			continue
		}

		words[0] = trim(low(words[0]))
		switch words[0] { // Depending on the first word
		case "uci":
			handleUCI()
		case "isready":
			handleIsReady()
		case "setoption":
			handleSetOption(cmd)
		case "stop":
			handleStop(toEng)
		case "quit", "q":
			quit = true
			continue
		}
	}
}

func handleUCI() {
	tell("id name TsarMate")
	tell("id author KcivazB")

	tell("option name hash type spin 32 min 1 max 1024")
	tell("option name Threads type spin default 1 min 1 max 16")

	tell("uciok")
}

func handleIsReady() {
	tell("readyok")
}

func handleSetOption(option string) {
	tell("info string set option", option)
	tell("info string not implemented yet")
}

func handleBestMove(bm string) {
	tell(bm)
}

func handleStop(toEng chan string) {
	toEng <- "stop"
}

func input() chan string {
	line := make(chan string)
	go func() { // Start an anonymous go routine inside the function.
		reader := bufio.NewReader(os.Stdin)
		for {
			text, err := reader.ReadString('\n')
			text = strings.TrimSpace(text)
			if err != io.EOF && len(text) > 0 {
				line <- text
			}
		}
	}()
	return line
}

func mainTell(text ...string) {
	toGUI := ""
	for _, t := range text {
		toGUI += t + " "
	}
	fmt.Println(strings.TrimSpace(toGUI))
}

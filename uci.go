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

var bestMove = ""

func uci(input chan string) {
	tell("info string Hello from uci")
	toEng, fromEng := engine()
	bInfinite := false

	var cmd string
	var bm string

	quit := false
	for !quit {
		select {
		case cmd = <-input:
		case bm = <-fromEng:
			// Get the best move from the engine
			handleBestMove(bm, bInfinite) //Handle the best move
			continue
		}
		words := strings.Split(cmd, " ") // Get the words from the GUI
		words[0] = trim(low(words[0]))
		switch words[0] { // Depending on the first word
		case "uci":
			handleUCI()
		case "setoption":
			handleSetOption(cmd)
		case "isready":
			handleIsReady()
		case "ucinewgame":
			handleNewGame()
		case "position":
			handlePosition(words)
		case "debug":
			handleDebug(words)
		case "register":
			handleRegister(words)
		case "go":
			handleGo(words)
		case "ponderhit":
			handlePonderhit()
		case "stop":
			handleStop(toEng, &bInfinite)
		case "quit", "q":
			quit = true
			continue
		}
	}
}

func handlePonderhit() {
	tell("info string ponderhit not implemented yet")
}

func handleDebug(words []string) {
	tell("info string debug not implemented yet")
}

func handleGo(words []string) {
	if len(words) > 1 {
		words[1] = trim(low(words[1]))
		switch words[1] {
		case "searchmoves":
			tell("info string go searchmoves not implemented yet")
		case "ponder":
			tell("info string go ponder not implemented yet")
		case "wtime":
			tell("info string go wtime not implemented yet")
		case "btime":
			tell("info string go btime not implemented yet")
		case "winc":
			tell("info string go winc not implemented yet")
		case "binc":
			tell("info string go binc not implemented yet")
		case "movestogo":
			tell("info string go movestogo not implemented yet")
		case "depth":
			tell("info string go depth not implemented yet")
		case "nodes":
			tell("info string go nodes not implemented yet")
		case "movetime":
			tell("info string go movetime not implemented yet")
		case "mate":
			tell("info string go mate not implemented yet")
		case "infinite":
			tell("info string go infinite not implemented yet")

		default:
			tell("info string go ", words[1], " not implemented yet")
		}
	} else {
		tell("info string go not implemented yet")
	}

}

func handleRegister(words []string) {
	tell("info string register not implemented yet")
}

func handlePosition(words []string) {
	if len(words) > 1 {
		words[1] = trim(low(words[1]))
		switch words[1] {
		case "startpos":
			tell("info string position startpos not implemented yet")
		case "fen":
			tell("info string position fen not implemented yet")
		default:
			tell("info string position ", words[1], " not implemented yet")
		}
	}

}

func handleNewGame() {
	tell("info string ucinewgame not implemented yet")
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

func handleBestMove(bm string, bInfinite bool) {
	if bInfinite {
		bestMove = bm
	}
	tell(bestMove)
}

func handleStop(toEng chan string, bInfinite *bool) {
	if *bInfinite {
		if bestMove != "" { // If no best move yet
			tell(bestMove) // tell the GUI we have a best move
			bestMove = ""  // And we set it back to ""
		}
		toEng <- "stop" // Stop the engine function
		*bInfinite = false
	}
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

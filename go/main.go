package main

import "fmt"

func uci(frGUI chan string, tell func(text ...string)){
	tell("info string Hello from uci")
	fromEng, toEng := engine()
	quit := false
	cmd := ""
	for quit == false {
		selct {
		case cmd : <-frGUI
		}
		switch cmd {
		case "uci":
		case "stop":
		case "quit","q":
			quit = true
			continue
		}
	}
}

func input() chan string {
	line := make(chan string)
	go func() { // Start an anonymous go routine inside the function.
		var reader *bufio.reader
		reader = bufio.newReader(os.Stdin)
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


func mainTell(text ...string){
	toGUI:= ""
	for _,t := range text {
		toGUI += t
	}
	fmt.Println(toGUI)
}
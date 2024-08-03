package main

func engine() (fromEng, toEng chan string) {
	tell("info string Hello from Engine")
	fromEng = make(chan string)
	toEng = make(chan string)
	go func() {
		for cmd := range toEng {
			switch cmd {
			case "stop":
			case "quit":
			}
		}
	}()
	return
}

import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
/*
  This code is written to do everything but track the game history from the game object, which requires a major overhaul
*/

/*class Square extends React.Component {

  This whole block of code was the original way of defining a "Square", in a manner
  similar to object-oriented programming.
  Later on, the 'Square' object had all of its modifying functionality inherited from the Board class, making it a *controlled component*
  Below this is code that defines square as a *functional component*
  constructor(props) {
    super(props);
    this.state = {
      value: null,
    };
  }
  This constructor was made for the squares to track information, not the board
  in the end, the Board was designed to track information


  render() {
    return (
      <button
        className="square"
        onClick={() => this.props.onClick()}
      >
        {this.props.value}
      </button>
      the 'onClick' line is written as such to pass a function as an object. the => makes sure the right *this* is called
    );
  }
}
*/

/*
Functional components are a simpler way of coding parts of a program
All they do is have a 'render' method and don't have their own data
The function just takes props (a 'properties' object that's kind of like metadata for
a class) and is told what to output
*/

function Square(props) {
  return (
    <button className="square" onClick={props.onClick}>
      {props.value}
    </button>
  );
  /*
  Just takes in a set of properties, sticks the relevant parts on an HTML button
  instance, and sends it back as code
  side note: no need for the arrow in the onClick declaration to access the correct *this* value
  */
}

class Board extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      squares: Array(9).fill(null),
      xIsNext: true, //set the initial state of the game
    };
  }

  handleClick(i){
    const squares = this.state.squares.slice();     //slice() creates a copy of the array for use within the handleClick() function

    if (calculateWinner(squares) || squares[i]) { //if someone won, do nothing upon being clicked
      return;
    }
    squares[i] = this.state.xIsNext ? 'X':'O';
    //shorthand boolean to change the value in this array based on whose turn
    //below: update the copied array, i.e. in this scope
    this.setState({
      squares: squares,
      xIsNext: !this.state.xIsNext, //flip turns
    });
    //update the original squares[] array, i.e. re render it

    /*Why make a copy array?
      We could modify the original squares array directly, but the copy-update-replace helps us keep a ledger of each square's state over timeÔ
    */

    //all functionality wrt writing and updating values is now under the Board{} code
    //this is all the functionality we need
    //this makes each square a *controlled component*


  }

  renderSquare(i) {
    return (
      <Square
        value={this.state.squares[i]}
        onClick={() => this.handleClick(i)}
      />
    );
    /*renders an HTML Square element with the property value equal to its corresponding value in the squares array declared in the Board constructor */

  }
  //render() is called over and over again

  render() {
    const winner = calculateWinner(this.state.squares);
    let status;
    if (winner) {
      status = 'Winner: ' + winner;
    } else {
      status = 'Next player: ' + (this.state.xIsNext ? 'X' : 'O');
    }
    //shorthand boolean math to decide whose name is in the 'Next Player' announcement

        // Below: standard syntax for "React, display this on the HTML page"
        // note that it's entirely HTML code
        // also note that neither HTML nor javascript comments will be compiled as such for some reason
    return (
      <div>
        <div className="status">{status}</div>
        <div className="board-row">
          {this.renderSquare(0)}
          {this.renderSquare(1)}
          {this.renderSquare(2)}
        </div>
        <div className="board-row">
          {this.renderSquare(3)}
          {this.renderSquare(4)}
          {this.renderSquare(5)}
        </div>
        <div className="board-row">
          {this.renderSquare(6)}
          {this.renderSquare(7)}
          {this.renderSquare(8)}
        </div>
      </div>
    );
  }
}

class Game extends React.Component {
  render() {
    return (
      <div className="game">
        <div className="game-board">
          <Board />
        </div>
        <div className="game-info">
          <div>{/* status */}</div>
          <ol>{/* TODO */}</ol>
        </div>
      </div>
    );//<Board /> returns a Board object, i.e. the html generated in the return() function in Board
  }
}

// ========================================

ReactDOM.render(
  <Game />,
  document.getElementById('root')
);

//Code to calculate the winner based on all the different lines you can make on a tic-tac-toe board
//mostly barebones javascript. stick this block of code anywhere in the file and you can reference it from anywhere

function calculateWinner(squares) {
  const lines = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6],
  ];
  //logic that checks across this set of sets of coordinates

  for (let i = 0; i < lines.length; i++) {
    const [a, b, c] = lines[i];
    if (squares[a] && squares[a] === squares[b] && squares[a] === squares[c]) {
      return squares[a];
    }
  }
  return null;
}

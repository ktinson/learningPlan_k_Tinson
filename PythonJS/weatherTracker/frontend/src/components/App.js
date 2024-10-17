import React, {Component} from "react";
import ReactDOM from 'react-dom/client'; 
export default class App extends Component{
    constructor(props){ 
        super(props)
    }
    render(){
        return <h1>Testing the Front End</h1>
    }
}
const root = ReactDOM.createRoot(
    document.getElementById('app')
  );
  const element = <h1>Hello, world</h1>;
  root.render(<App/>);
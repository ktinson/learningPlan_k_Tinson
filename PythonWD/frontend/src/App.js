import React, { Component } from "react";
import Modal from "./components/Modal";
import axios from "axios";

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      viewLarge: false,
      cardList: [],
      modal: false,
      activeItem: {
        name: "",
        description: "",
        large: false,
      },
    };
  }
  
  
  componentDidMount() {
    this.refreshList();
  }
  
  refreshList = () => {
    
    axios
      .get("http://localhost:8000/api/cards/")
      .then((res) => this.setState({ cardList: res.data }))
      .catch((err) => console.log(err));
   
  };

  toggle = () => {
    this.setState({ modal: !this.state.modal });
  };

  handleSubmit = (item) => {
    this.toggle();

    if (item.id) {
      axios
        .put(`http://localhost:8000/api/cards/${item.id}/`, item)
        .then((res) => this.refreshList());
      return;
    }
    axios
      .post("http://localhost:8000/api/cards/", item)
      .then((res) => this.refreshList());
  };

  handleDelete = (item) => {
    axios
      .delete(`http://localhost:8000/api/cards/${item.id}/`)
      .then((res) => this.refreshList());
  };

  createItem = () => {
    const item = { name: "", description: "", large: false };

    this.setState({ activeItem: item, modal: !this.state.modal });
  };

  editItem = (item) => {
    this.setState({ activeItem: item, modal: !this.state.modal });
  };

  displayLarge = (status) => {
    if (status) {
      return this.setState({ viewLarge: true });
    }

    return this.setState({ viewLarge: false });
  };

  renderTabList = () => {
    return (
      <div className="nav nav-tabs">
        <span
          onClick={() => this.displayLarge(true)}
          className={this.state.viewLarge ? "nav-link active" : "nav-link"}
        >
          Large Cards
        </span>
        <span
          onClick={() => this.displayLarge(false)}
          className={this.state.viewLarge ? "nav-link" : "nav-link active"}
        >
          Small Cards
        </span>
      </div>
    );
  };

  renderItems = () => {
    const { viewLarge } = this.state;
    const newItems = this.state.cardList.filter(
      (item) => item.large === viewLarge
    );

    return newItems.map((item) => (
      <li
        key={item.id}
        className="list-group-item d-flex justify-content-between align-items-center"
      >
        <span
          className={`card-name mr-2 ${
            this.state.viewLarge ? "Large-card" : ""
          }`}
          description={item.description}
        >
          {item.name}
        </span>
        <span>
          <button
            className="btn btn-secondary mr-2"
            onClick={() => this.editItem(item)}
          >
            Edit
          </button>
          <button
            className="btn btn-danger"
            onClick={() => this.handleDelete(item)}
          >
            Delete
          </button>
        </span>
      </li>
    ));
  };

  render() {
    return (
      <main className="container">
        <h1 className="text-white text-uppercase text-center my-4">Card app</h1>
        <div className="row">
          <div className="col-md-6 col-sm-10 mx-auto p-0">
            <div className="card p-3">
              <div className="mb-4">
                <button
                  className="btn btn-primary"
                  onClick={this.createItem}
                >
                  Add Card
                </button>
              </div>
              {this.renderTabList()}
              <ul className="list-group list-group-flush border-top-0">
                {this.renderItems()}
              </ul>
            </div>
          </div>
        </div>
        {this.state.modal ? (
          <Modal
            activeItem={this.state.activeItem}
            toggle={this.toggle}
            onSave={this.handleSubmit}
          />
        ) : null}
      </main>
    );
  }
  
}

export default App;
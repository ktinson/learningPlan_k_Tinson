import React, { Component } from "react";
import Modal from "./components/Modal";
import {Button, CardActions, Typography, CardContent, CardMedia, Card, Grid} from '@mui/material/';

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

    return( <Grid container spacing={3}> {newItems.map((item) => {
      return(
        <>
        <Grid size={8} style={{padding: "25px"}}>
        <Card sx={{ width: 290 }}>
      <CardMedia
        sx={{ height: 345 }}
        image={item.image}
        title="card image"
      />
      <CardContent>
        <Typography gutterBottom variant="h5" component="div">
          <h1>{item.name}</h1>
        </Typography>
        <Typography variant="body2" sx={{ color: 'text.secondary' }}>
          <p>{item.description}</p>
        </Typography>
      </CardContent>
      <CardActions>
      <Button
            className="btn btn-secondary mr-2"
            onClick={() => this.editItem(item)}
          >
            Edit
          </Button>
          <Button
            className="btn btn-danger"
            onClick={() => this.handleDelete(item)}
          >
            Delete
          </Button>
      </CardActions>
    </Card>
    </Grid>
      </>)
  })}</Grid>);
  };

  render() {
    return (
      <main className="container">
        <h1 className="text-Black text-uppercase text-center my-4">Card app</h1>
        <div className="">
              <div className="mb-4">
                <Button className="btn btn-primary" onClick={this.createItem}>
                  Add Card
                </Button>
              </div>
              {this.renderTabList()}
              <div style={{padding: "50px"}}>
                {this.renderItems()}
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
import React, { useState } from "react";
import axios from "axios";
// import "./RestAPI.css";

function RestAPI() {
  const [text, setText] = useState([]);

  return (
    <>
      <h1>REST API 연습</h1>
      <div className="btn-primary">
          <input type="text" id="title"/>
          <p></p>
          <textarea id="content" cols="30" rows="10"></textarea>
          <p></p>
        <button
          onClick={() => {
              let getTitle = document.getElementById("title").value;
            let getContent = document.getElementById("content").value;
            axios
              .post("http://127.0.0.1:8000/review/", {
                title: getTitle,
                content: getContent,
              })
              .then(function (response) {
                console.log(response);
                document.getElementById("title").value=null;
            document.getElementById("content").value=null;
              })
              .catch(function (error) {
                console.log(error);
              });
          }}
        >
          POST
        </button>
        <button
          onClick={() => {
            axios
              .get("http://127.0.0.1:8000/review/")
              .then((response) => {
                setText([...response.data]);
                console.log(response.data);
              })
              .catch(function (error) {
                console.log(error);
              });
          }}
        >
          GET
        </button>
      </div>
      {text.map((e) => (
        <div>
          {" "}
          <div className="list">
            <span>
              {e.id}번, {e.title}, {e.content}, {e.updated_at}
            </span>
            <button
              className="btn-delete"
              onClick={() => {
                axios.delete(`http://127.0.0.1:8000/review/${e.id}`);
                setText(text.filter((text) => text.id !== e.id));
              }}
            >
              DELETE
            </button>{" "}
          </div>
        </div>
      ))}
    </>
  );
}

export default RestAPI;
import React from 'react';
// import ReactDOM from 'react-dom';
import { render } from 'react-dom';
import BooksList from './App';

render(
    <BooksList url='/api/' pollInterval={1000}/>,
    document.getElementById('container')
);

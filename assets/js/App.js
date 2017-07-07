import React, {Component} from 'react';


class BooksList extends Component {
    constructor(props) {
        super(props);
        this.state = {
            data: []
        };
        this.loadBooksFromServer = this.loadBooksFromServer.bind(this);

    }

    loadBooksFromServer() {
        fetch(this.props.url)
            .then((response) => {
                return response.json()
            })
            .then((json) => {
                this.setState({data: json});
            });
    }

    componentDidMount() {
        this.loadBooksFromServer();
        setInterval(this.loadBooksFromServer, this.props.pollInterval);
    }

    render() {
        const {
            pollInterval
        } = this.props;

        let bookNodes = this.state.data.map(function (book) {
            return <li key={book.title}>
                Title: {book.title} <br/>
                Author: {book.author}
            </li>

        });

        return (
            <div>
                <h1>Hello React!</h1>
                <ul>
                    {bookNodes}
                </ul>
            </div>
        )
    }
}

export default BooksList;

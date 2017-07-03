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
        $.ajax({
            url: this.props.url,
            datatype: 'json',
            cache: false,
            success: function (data) {
                this.setState({data: data});
            }.bind(this)
        })
    }

    componentDidMount() {
        this.loadBooksFromServer();
        setInterval(this.loadBooksFromServer, this.props.pollInterval);
    }

    render() {
        const {
            pollInterval
        } = this.props;
        if (this.state.data) {
            console.log("DATA WOO");
            const bookNodes = this.state.data.map(function (book) {
                return <li>{book.title}</li>
            })
        }
        return (
            <div>
                <h1>Hello React!</h1>
                <ul>
                    {this.data}
                </ul>
            </div>
        )
    }
}

export default BooksList;

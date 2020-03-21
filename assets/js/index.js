import React from 'react'
import ReactDOM from 'react-dom'


import { TransformWrapper, TransformComponent } from 'react-zoom-pan-pinch';

class Page extends React.Component {
    render() {
        var list = window.props;
        return <div>{list.map(item => <Post key={item.pk} position_x={item.post_position_x}
                                                 position_y={item.position_y}
                                                 title={item.title} text={item.text}/> )}</div>;
    }
}

class Post extends React.Component {
    render() {
     return <li><b>{this.props.title}</b></li>;
    }
}


ReactDOM.render(
    <Page/>,
    window.react_mount,
);
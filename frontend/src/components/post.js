import 'index.scss';

export const Post = (props) => {
    return (<div key={props.paper.id} class="content-container mt-5">
        {JSON.stringify(props.paper)}
    </div>)
}
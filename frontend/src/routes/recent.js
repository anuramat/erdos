import 'papers.scss';
import 'bootstrap/dist/css/bootstrap.min.css';
import { Papers, Tabs } from 'components/papers';

export const Recent = () => {

    return (
        <Papers tab={Tabs.recent}>
            <div className="content-container">
                nothing here yet
            </div>
        </Papers>
    )

}


import React from 'react';
import NegotiatorProfile from '../components/NegotiatorProfile';
import OpponentProfile from '../components/OpponentProfile';
import OutcomeScenarios from '../components/OutcomeScenarios';

const Dashboard = () => {
    return (
        <div>
            <NegotiatorProfile />
            <OpponentProfile />
            <OutcomeScenarios />
        </div>
    );
};

export default Dashboard; 
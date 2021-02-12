import React from "react"

import HistoryCard from "../components/cards/HistoryCard"

export default function Stats () {
    const historyCards = dataset.map(datapoint => <HistoryCard historyData={datapoint}/>)
    return (
        <div>
            {historyCards}
        </div>
    )
}

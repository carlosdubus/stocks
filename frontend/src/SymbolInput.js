import { AsyncTypeahead } from 'react-bootstrap-typeahead';
import React, { useState } from 'react';

const SEARCH_URI = '/api/stocks/symbols';

function SymbolInput({ onChange }) {
    const [isLoading, setIsLoading] = useState(false);
    const [options, setOptions] = useState([]);

    const handleSearch = (query) => {
        if (options.length > 0) {
            return;
        }
        setIsLoading(true);

        fetch(`${SEARCH_URI}`)
            .then((resp) => resp.json())
            .then(items => {
                const options = items.map(row => row.symbol);
                console.log(options);
                setOptions(options);
                setIsLoading(false);
            });
    };
    return (
        <AsyncTypeahead
            onChange={onChange}
            id="async-example"
            isLoading={isLoading}
            labelKey="login"
            minLength={1}
            onSearch={handleSearch}
            options={options}
            placeholder="Search for symbol..."
        />
    );
}

export default SymbolInput;
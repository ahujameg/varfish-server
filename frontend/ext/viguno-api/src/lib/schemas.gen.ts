// This file is auto-generated by @hey-api/openapi-ts

export const $HpoTerm = {
    type: 'object',
    description: 'Struct for loading an HPO term from JSON.',
    required: ['term_id'],
    properties: {
        term_id: {
            type: 'string',
            description: 'The term ID.'
        },
        term_name: {
            type: 'string',
            description: 'The term name (optional).',
            nullable: true
        }
    }
} as const;

export const $IcBasedOn = {
    type: 'string',
    description: `Enum for representing the information content kind.

We replicate what is in the \`hpo\` create so we can put them on the command line and use
them in HTTP queries more easily.`,
    enum: ['gene', 'omim']
} as const;

export const $Match = {
    type: 'string',
    description: 'Specify how to perform query matches in the API calls.',
    enum: ['exact', 'prefix', 'suffix', 'contains']
} as const;

export const $Query = {
    type: 'object',
    title: 'HpoSimTermGeneQuery',
    description: `Parameters for \`handle\`.

This allows to compute differences between

- \`terms\` -- set of terms to use as query
- \`gene_ids\` -- set of ids for genes to use as "database", can be NCBI\
gene ID or HGNC gene ID.
- \`gene_symbols\` -- set of symbols for genes to use as
"database"`,
    required: ['terms'],
    properties: {
        terms: {
            type: 'array',
            items: {
                type: 'string'
            },
            description: 'Set of terms to use as query.'
        },
        gene_ids: {
            type: 'array',
            items: {
                type: 'string'
            },
            description: 'The set of ids for genes to use as "database".',
            nullable: true
        },
        gene_symbols: {
            type: 'array',
            items: {
                type: 'string'
            },
            description: 'The set of symbols for genes to use as "database".',
            nullable: true
        }
    }
} as const;

export const $ResponseQuery = {
    type: 'object',
    title: 'HpoSimTermTermQuery',
    description: `Request as sent together with the response.

The difference is that the \`lhs\` and \`rhs\` fields are replaced by vecs.`,
    required: ['lhs', 'rhs'],
    properties: {
        lhs: {
            type: 'array',
            items: {
                type: 'string'
            },
            description: 'The one set of HPO terms to compute similarity for.'
        },
        rhs: {
            type: 'array',
            items: {
                type: 'string'
            },
            description: 'The second set of HPO terms to compute similarity for.'
        },
        ic_base: {
            '$ref': '#/components/schemas/IcBasedOn'
        },
        similarity: {
            '$ref': '#/components/schemas/SimilarityMethod'
        },
        combiner: {
            '$ref': '#/components/schemas/ScoreCombiner'
        }
    }
} as const;

export const $Result = {
    type: 'object',
    title: 'HpoSimTermTermResult',
    description: 'Result container.',
    required: ['version', 'query', 'result'],
    properties: {
        version: {
            '$ref': '#/components/schemas/Version'
        },
        query: {
            '$ref': '#/components/schemas/ResponseQuery'
        },
        result: {
            type: 'array',
            items: {
                '$ref': '#/components/schemas/ResultEntry'
            },
            description: 'The resulting records for the scored genes.'
        }
    }
} as const;

export const $ResultEntry = {
    type: 'object',
    title: 'HpoSimTermTermResultEntry',
    description: 'Result entry for `handle`.',
    required: ['lhs', 'rhs', 'score'],
    properties: {
        lhs: {
            type: 'string',
            description: 'The lhs entry.'
        },
        rhs: {
            type: 'string',
            description: 'The rhs entry.'
        },
        score: {
            type: 'number',
            format: 'float',
            description: 'The similarity score.'
        }
    }
} as const;

export const $ResultGene = {
    type: 'object',
    description: 'Representation of a gene.',
    required: ['ncbi_gene_id', 'gene_symbol'],
    properties: {
        ncbi_gene_id: {
            type: 'integer',
            format: 'int32',
            description: 'The HPO ID.',
            minimum: 0
        },
        gene_symbol: {
            type: 'string',
            description: 'The description.'
        },
        hgnc_id: {
            type: 'string',
            description: 'The HGNC ID.',
            nullable: true
        }
    }
} as const;

export const $ResultHpoTerm = {
    type: 'object',
    description: 'Representation of an HPO term.',
    required: ['term_id', 'name'],
    properties: {
        term_id: {
            type: 'string',
            description: 'The HPO ID.'
        },
        name: {
            type: 'string',
            description: 'The term name.'
        }
    }
} as const;

export const $Result_ = {
    type: 'object',
    title: 'HpoTermsResult',
    description: 'Container for the result.',
    required: ['version', 'query', 'result'],
    properties: {
        version: {
            '$ref': '#/components/schemas/Version'
        },
        query: {
            '$ref': '#/components/schemas/Query'
        },
        result: {
            type: 'array',
            items: {
                '$ref': '#/components/schemas/ResultEntry'
            },
            description: 'The resulting records for the scored genes.'
        }
    }
} as const;

export const $ScoreCombiner = {
    type: 'string',
    description: `Representation of the standard combiners from HPO.

We replicate what is in the \`hpo\` create so we can put them on the command line and use
them in HTTP queries more easily.`,
    enum: ['fun-sim-avg', 'fun-sim-max', 'bma']
} as const;

export const $SimilarityMethod = {
    type: 'string',
    description: `Enum for representing similarity method to use.

We replicate what is in the \`hpo\` create so we can put them on the command line and use
them in HTTP queries more easily.`,
    enum: ['distance-gene', 'graph-ic', 'information-coefficient', 'jc', 'lin', 'mutation', 'relevance', 'resnik']
} as const;

export const $TermDetails = {
    type: 'object',
    title: 'HpoSimTermGeneTermDetails',
    description: 'Detailed term scores.',
    required: ['term_gene', 'score'],
    properties: {
        term_query: {
            allOf: [
                {
                    '$ref': '#/components/schemas/HpoTerm'
                }
            ],
            nullable: true
        },
        term_gene: {
            '$ref': '#/components/schemas/HpoTerm'
        },
        score: {
            type: 'number',
            format: 'float',
            description: 'The similarity score.'
        }
    }
} as const;

export const $Version = {
    type: 'object',
    description: 'Version information that is returned by the HTTP server.',
    required: ['hpo', 'viguno'],
    properties: {
        hpo: {
            type: 'string',
            description: 'Version of the HPO.'
        },
        viguno: {
            type: 'string',
            description: 'Version of the `viguno` package.'
        }
    }
} as const;
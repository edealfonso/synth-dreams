const path = require('path');
const webpack = require('webpack');
const BundleTracker = require('webpack-bundle-tracker');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const CssMinimizerPlugin = require('css-minimizer-webpack-plugin');

// A single config for development and production; the mode comes from the CLI:
// - development: `webpack --mode development --watch` (npm run watch)
// - production: `webpack --mode production` (npm run build), which also runs postcss
module.exports = (env, argv) => {
    const isProd = argv.mode === 'production';

    return {
        context: __dirname,
        mode: isProd ? 'production' : 'development',
        devtool: 'source-map',
        entry: './static/js/main.js', // app entry point: imports the other JS modules and the SCSS

        output: {
            path: path.resolve(__dirname, 'static/bundles'),
            publicPath: '/static/bundles/',
            filename: '[name]-[fullhash].js',
            clean: true,
        },

        plugins: [
            new BundleTracker({ filename: './webpack-stats.json' }),
            new MiniCssExtractPlugin({ filename: 'styles.[contenthash].css' }),
            // global jQuery as `$` in every module, without importing it
            new webpack.ProvidePlugin({ $: 'jquery', jQuery: 'jquery' }),
        ],

        module: {
            rules: [
                {
                    test: /\.js$/,
                    exclude: /node_modules/,
                    loader: 'babel-loader',
                },
                {
                    test: /\.s?css$/i,
                    use: [
                        MiniCssExtractPlugin.loader,
                        { loader: 'css-loader', options: { sourceMap: true } },
                        // postcss (CSS prefixes and polyfills) in production only
                        ...(isProd ? [{
                            loader: 'postcss-loader',
                            options: { postcssOptions: { plugins: ['postcss-preset-env'] } },
                        }] : []),
                        {
                            loader: 'sass-loader',
                            options: {
                                sassOptions: { outputStyle: 'expanded' },
                                sourceMap: true,
                            },
                        },
                    ],
                },
            ],
        },

        optimization: {
            minimizer: [
                '...', // keep webpack 5's default minimizers (terser) and add the CSS one
                new CssMinimizerPlugin(),
            ],
        },
    };
};

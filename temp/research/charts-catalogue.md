# Chart catalogue and interface standard (research)

Status: research input, not a decision. Language: English. Written 2026-11-06.
Marker ⚠️ = not verified against a primary source in this session (from general knowledge or an incomplete fetch).

## 0. Sources and retrieval

All retrieved 2026-11-06 unless noted.

| Source | URL | Used for | Result |
|---|---|---|---|
| From Data to Viz | https://www.data-to-viz.com/ | decision tree by data type, caveats | fetched; page text partly scrambled, grouping approximate |
| FT Visual Vocabulary (chart-doctor) | https://github.com/Financial-Times/chart-doctor/blob/main/visual-vocabulary/README.md | 9 relationship categories | fetched |
| Data Viz Catalogue | https://datavizcatalogue.com/methods/ and /search/ | function-based catalogue | **HTTP 403, not retrieved.** Names from it are only from memory ⚠️ |
| Vega example gallery | https://vega.github.io/vega/examples/ | example names | fetched |
| Vega-Lite marks | https://vega.github.io/vega-lite/docs/mark.html | mark list | fetched |
| Apache ECharts series list | https://echarts.apache.org/en/llms.txt (index of option docs) | series types | fetched; the examples page itself returned only navigation |
| Charming (ECharts for Rust) | https://github.com/yuankunzhang/charming | Rust, chart types | fetched |
| Vega-Lite spec docs | https://vega.github.io/vega-lite/docs/spec.html | schema URL, data/encoding split | fetched |
| Vega-Lite repo | https://github.com/vega/vega-lite | licence | fetched |
| vl-convert | https://github.com/vega/vl-convert | Rust rendering of Vega(-Lite) | fetched |
| vega_lite_4 crate | https://docs.rs/crate/vega_lite_4/latest | Rust typed bindings | search snippet only |
| Observable Plot | https://github.com/observablehq/plot | licence | fetched; no spec statement found |
| plotly.js | https://github.com/plotly/plotly.js | licence | fetched; schema not mentioned on page |
| plotly.rs | https://github.com/plotly/plotly.rs | Rust binding | fetched |
| Apache ECharts | https://github.com/apache/echarts | licence | fetched |
| Apache arrow-rs | https://github.com/apache/arrow-rs | Rust Arrow | fetched; page says nothing on spec status |
| WAI-ARIA Graphics Module 1.0 | https://www.w3.org/TR/graphics-aria-1.0/ | roles | fetched |
| capnproto-rust | https://github.com/capnproto/capnproto-rust | plugin IPC | fetched |
| wit-component README | https://github.com/bytecodealliance/wasm-tools/blob/main/crates/wit-component/README.md | WIT / components | fetched |
| Blinc chart source | `/srv/FreeSynergy/fs-documentation/.research-blinc/crates/blinc_cn/src/components/chart/` | section 2 | read locally |
| Our chart docs | `/srv/FreeSynergy/fs-documentation/docs/en/components/widgets/data/chart/` | section 2 | read locally |

Not consulted, named only from background knowledge ⚠️: Wilkinson, *The Grammar of Graphics* (Springer, 1999/2005); Wickham, "Tidy Data" (J. Statistical Software, 2014); Apache Arrow format spec (arrow.apache.org); Plotly `plot-schema.json`; Tufte, Few, Cleveland (perceptual ranking); Likert-plot literature (Robbins and Heiberger); Gantt/PM literature.

## 1. Catalogue by purpose

Legend.
- **Data shape** notation: `C` category, `N` number, `T` time, `G` geo (point/area), `R` row set, `S` set membership, `Edge` source,target[,weight], `Tree` parent/child hierarchy, `Iv` interval start,end, `Dist` raw sample of N, `Mat` matrix C x C -> N.
- **Priority**: A now, B soon, C later. Chosen by what surveys, project management and ERP need first.
- **Blinc today?** "yes" = exists in the Blinc `cn` chart module (section 2); "partly" = reachable via options; "no".
- Multi-listed charts appear once, in their primary purpose, with a note.

### 1.1 Compare (magnitude, ranking, deviation)

| Chart | Answers | Data shape | Prio | Blinc today? |
|---|---|---|---|---|
| Column chart (vertical bar) | How big is each category? | C,N | A | yes (`bar_chart`) |
| Bar chart (horizontal) | Same, long labels | C,N | A | yes (`.horizontal()`) |
| Grouped (clustered) bar | Compare sub-categories side by side | C,C,N | A | yes (multi-series) |
| Ordered bar/column (ranking) | Who is first, who is last? | C,N sorted | A | partly (caller sorts) |
| Paired bar/column | Two values per category | C,N,N | B | yes (`comparison_bar_chart`) |
| Lollipop | Ranking with less ink than bars | C,N | B | no |
| Dot plot / Cleveland dot | Compare values on a common scale, many categories | C,N | B | no |
| Dot strip plot | Values of items along one axis, several groups | C,N | C | no |
| Slope chart | Change between two points per item | C,N,N | B | no |
| Dumbbell | Gap between two values per category | C,N,N | B | partly (comparison) |
| Bump chart | How does rank change over time? | C,T,rank | C | no |
| Proportional symbol (ordered) | Magnitude via symbol area | C,N | C | no |
| Bullet chart | Actual vs target vs ranges | C,N,N,ranges | A | partly (bands + marker, no bullet shape) |
| Diverging bar | Deviation from a mid value, positive/negative | C,N signed | A | no |
| Diverging stacked bar | Deviation split by level (see 1.12) | C,C,N | A | no |
| Spine chart | Split of a total into two/three parts per item, normalised | C,N,N | C | no |
| Surplus/deficit filled line | Where a series is above/below another | T,N,N | C | no |
| Radar / spider | Profile of one item over several axes | C,N (axes) | B | no (docs promise it) |
| Parallel coordinates | Compare many items over many dimensions | R (N cols) | C | no |
| Pictogram / isotype | Counts as repeated icons | C,N | C | no |
| Pictorial bar (ECharts) | Bar with icon fill | C,N | C | no |
| Rose / Nightingale (polar bar) | Magnitudes around a circle | C,N | C | no |
| Radial bar / circular bar | Compact magnitude comparison | C,N | C | no |
| Word cloud | Which terms dominate in free text? | term,N | B | no |
| Bar with error bars / interval | Value with uncertainty | C,N,N,N | B | no |
| Marimekko (variable-width stacked) | Two-way share with sizes | C,C,N | C | no |
| Small multiples (faceting) | Same chart per group | any + C | B | no (composition, not a type) |

### 1.2 Part of whole

| Chart | Answers | Data shape | Prio | Blinc today? |
|---|---|---|---|---|
| Pie | Share of a whole, few parts | C,N | A | yes (`pie_chart`) |
| Donut | Same, with total in the hole | C,N | A | yes (`.donut()`) |
| Stacked bar/column | Totals and parts | C,C,N | A | yes (`.stacked()`) |
| 100 % stacked bar/column (proportional) | Shares per category | C,C,N | A | no (only absolute stacking) |
| Stacked area | Parts of a total over time | T,C,N | A | yes |
| 100 % stacked area | Share over time | T,C,N | B | no |
| Treemap | Shares in a hierarchy | Tree,N | B | no |
| Sunburst | Hierarchy shares, radial | Tree,N | C | no |
| Circle packing | Hierarchy shares by circles | Tree,N | C | no |
| Waffle / grid plot | Percent as 10x10 squares | C,N | B | no |
| Waterfall | How parts add up/subtract to a total | C,N signed | A | no (also finance) |
| Voronoi treemap | Part of whole, irregular cells | C,N | C | no |
| Arc / half-donut (semi-circle) | Share, parliament-style outline | C,N | B | no |
| Venn / Euler | Overlap of sets (counts) | S,N | C | no |
| Funnel | Drop-off through stages | C ordered,N | B | no |
| Nested donut / multi-level pie | Two levels of share | Tree,N | C | no |
| Mosaic plot | Association of two categorical variables | C,C,N | C | no |
| Stacked bar with total label | Parts and total | C,C,N | A | partly |

### 1.3 Distribution

| Chart | Answers | Data shape | Prio | Blinc today? |
|---|---|---|---|---|
| Histogram | How are values spread? | Dist | A | yes (`histogram`, bins, log) |
| Density plot (KDE) | Smoothed spread | Dist | B | no |
| Boxplot | Median, quartiles, outliers | Dist per C | A | no |
| Violin | Shape of spread per group | Dist per C | B | no |
| Ridgeline (joy plot) | Spread of many groups, stacked | Dist per C | C | no |
| Strip / jitter plot | Raw points per group | Dist per C | B | no |
| Beeswarm | Raw points without overlap | Dist per C | C | no |
| Barcode plot | 1-D marks of every value | Dist | C | no |
| Cumulative distribution (ECDF) | Share below a value | Dist | B | no |
| Quantile-quantile plot | Does data follow a theory? | Dist,Dist | C | no |
| Population pyramid | Two-sided age/sex distribution | C,N,N | B | no |
| 2-D histogram / hexbin | Joint density, many points | N,N | C | no |
| Density 2-D / contour | Joint density, smoothed | N,N | C | no |
| Binned scatter | Overplotting avoided | N,N | C | no |
| Frequency polygon | Histogram as line | Dist | C | no |
| Quantile dot plot | Uncertainty as countable dots | Dist | C | no |
| Hypothetical outcome plot | Uncertainty as animation | Dist | C | no |
| Rug plot | Raw positions on an axis | Dist | C | no |
| Stem-and-leaf | Text histogram | Dist | C | no |

### 1.4 Change over time

| Chart | Answers | Data shape | Prio | Blinc today? |
|---|---|---|---|---|
| Line | Trend over time | T,N | A | yes |
| Multi-line | Several trends | T,C,N | A | yes |
| Smooth/step line | Interpolation choice | T,N | A | yes (`ChartCurve`) |
| Area | Volume over time | T,N | A | yes |
| Stacked area | See 1.2 | | A | yes |
| Streamgraph / ThemeRiver | Shifting composition, centred | T,C,N | C | no |
| Sparkline | Trend beside text | T,N | A | yes (`spark_line`) |
| Column over time | Discrete periods | T,N | A | yes |
| Line + column (combo) | Two measures, different units | T,N,N | B | no (one value axis) |
| Dual-axis line | Same, two axes | T,N,N | B | no |
| Calendar heatmap | Daily pattern over a year | T(day),N | B | no |
| Horizon graph | Many dense series in little height | T,N | C | no |
| Fan chart | Forecast with widening range | T,N,N,N | B | partly (bands are static value ranges, not time-dependent) |
| Confidence band / error band | Uncertainty over time | T,N,N,N | B | no |
| Connected scatterplot | Two measures traced through time | T,N,N | C | no |
| Cycle plot / seasonal subseries | Seasonality | T,C,N | C | no |
| Slopegraph | See 1.1 | | B | no |
| Stock price (OHLC) | See 1.14 | | B | no |
| Timeline (events) | What happened when? | T,label | B | no |
| Priestley / circle timeline | Lifespans or events | Iv | C | no |
| Seismogram | Dense signal | T,N | C | no |
| Small-multiple lines | Many series side by side | T,C,N | B | no |
| Moving average overlay | Trend smoothing | T,N | B | no |
| Warming stripes | Colour per period | T,N | C | no |
| Trend with markers/thresholds | Value vs limit over time | T,N + limits | A | yes (`threshold_line_chart`, bands, markers) |

### 1.5 Relationship (correlation)

| Chart | Answers | Data shape | Prio | Blinc today? |
|---|---|---|---|---|
| Scatter | Do two measures move together? | N,N | A | no (docs promise it) |
| Bubble | Third measure as size | N,N,N | B | no |
| Scatter with colour/shape category | Group effect | N,N,C | B | no |
| Scatter with regression line | Fitted trend | N,N + model | B | no |
| Scatter matrix (SPLOM) | All pairs of measures | R | C | no |
| Correlogram / correlation matrix | Strength of pairwise correlation | Mat | B | no |
| Heatmap (XY) | Value per cell of two categories | C,C,N | A | no (docs promise it) |
| Clustered heatmap | Heatmap with row/col clustering | Mat + Tree | C | no |
| Hexbin / 2-D density | See 1.3 | | C | no |
| Labelled scatter / quadrant chart | Items in four quadrants (e.g. effort/impact) | N,N,label | A | no |
| Trellis / faceted scatter | Relationship per group | N,N,C | C | no |
| 3-D scatter / surface | Three measures | N,N,N | C | no |
| Error bars / regression bands | Uncertainty | N,N,N | C | no |
| PCA biplot | Latent structure | R | C | no |
| Radial convergence / chord-type correlation | See 1.8 | | C | no |

### 1.6 Flow

| Chart | Answers | Data shape | Prio | Blinc today? |
|---|---|---|---|---|
| Sankey | Where does quantity go between stages? | Edge+weight | B | no |
| Alluvial | Same across several time points/categories | C per step,N | C | no |
| Chord diagram | Flows between groups, both directions | Mat | C | no |
| Waterfall | See 1.2 | | A | no |
| Funnel | See 1.2 | | B | no |
| Flow map | Flows between places | G,G,N | C | no |
| Arc diagram | Links in a 1-D order | Edge | C | no |
| Parallel sets | Category flows across dimensions | C,C,N | C | no |
| Process/flowchart (diagram, not chart) | Steps and decisions | Edge | C | no (diagram family, out of chart scope ⚠️) |
| Dependency wheel | Dependencies between modules | Edge | C | no |
| Sequence of events (swimlane) | Who does what in order | Iv/lane | C | no |
| Cumulative flow diagram | Work state over time (PM) | T,C,N | B | partly (stacked area) |

### 1.7 Hierarchy

| Chart | Answers | Data shape | Prio | Blinc today? |
|---|---|---|---|---|
| Tree (node-link) | Parent/child structure | Tree | B | no |
| Radial tree | Same, radial | Tree | C | no |
| Org chart | Reporting lines | Tree | B | no |
| Dendrogram | Cluster hierarchy | Tree + height | C | no |
| Treemap | See 1.2 | | B | no |
| Sunburst | See 1.2 | | C | no |
| Icicle / partition | Hierarchy as nested bars | Tree,N | C | no |
| Circle packing | See 1.2 | | C | no |
| Indented tree / outline | Large trees as text | Tree | C | no (widget, not chart) |
| Mind map | Brainstorm structure | Tree | C | no |
| Work breakdown structure (WBS) | Project decomposition | Tree | B | no |
| Cluster tree (phylogeny) | Hierarchical similarity | Tree | C | no |
| Bracket / tournament tree | Elimination rounds | Tree of matches | C | no |

### 1.8 Network

| Chart | Answers | Data shape | Prio | Blinc today? |
|---|---|---|---|---|
| Force-directed node-link | Who is connected to whom? | Edge,node attr | B | no |
| Adjacency matrix / reorderable matrix | Dense networks | Mat | C | no |
| Arc diagram | See 1.6 | | C | no |
| Hierarchical edge bundling | Many links over a hierarchy | Tree+Edge | C | no |
| Hive plot | Network with fixed axes | Edge,node attr | C | no |
| Chord | See 1.6 | | C | no |
| Matrix of dependencies (DSM) | Which module depends on which | Mat | C | no |
| Dependency graph / DAG | Task or package dependencies | Edge (acyclic) | B | no |
| Entity-relationship / UML (diagram) | Data model | Edge | C | no (diagram family ⚠️) |
| Graph (ECharts `graph`) | Network with layouts | Edge | B | no |
| Social-network ego graph | One actor's neighbours | Edge | C | no |

### 1.9 Geography

| Chart | Answers | Data shape | Prio | Blinc today? |
|---|---|---|---|---|
| Choropleth | Rate per region | G(area),N | B | no |
| Proportional symbol map / bubble map | Count per place | G(point),N | B | no |
| Dot-density map | Where do many events occur? | G(point) | C | no |
| Hexbin map | Density, hex bins | G(point) | C | no |
| Heat map (spatial) | Smooth density over space | G(point),N | C | no |
| Cartogram (contiguous / Dorling / equalised) | Region size = value | G(area),N | C | no |
| Flow / connection map | Links between places | G,G,N | C | no |
| Contour / isoline map | Continuous surface | G grid | C | no |
| Wind vectors | Direction and magnitude | G grid,vec | C | no |
| Globe (3-D) | Global data | G | C | no |
| Tile / hex map (grid cartogram) | Equal-size regions | G(area),N | C | no |
| Map with route/lines | Tracks, logistics | G(line) | C | no |
| Floor plan / seating map | Indoor occupancy ⚠️ | custom | C | no |

### 1.10 Project and schedule

| Chart | Answers | Data shape | Prio | Blinc today? |
|---|---|---|---|---|
| Gantt | Which task runs when, dependencies | Iv,C,Edge | A | no |
| Milestone timeline | Key dates | T,label | A | no |
| Roadmap (swimlane timeline) | Plan by theme/team | Iv,C | B | no |
| Burn-down | Work remaining vs plan | T,N,N | A | partly (line + marker) |
| Burn-up | Work done vs scope | T,N,N | A | partly (line) |
| Velocity chart | Work completed per sprint | C(sprint),N | B | yes (bar) |
| Cumulative flow diagram | See 1.6 | | B | partly |
| Kanban board (board, not chart) | State of work items | R by state | B | no (workbench component, not chart ⚠️) |
| Resource histogram / load chart | Allocation vs capacity per period | T,C,N,N | A | partly (stacked bar + marker) |
| Critical-path network (PERT) | Longest dependency chain | Edge,Iv | C | no |
| Baseline vs actual Gantt | Slippage | Iv,Iv | B | no |
| Earned value (S-curve) | Cost/schedule performance | T,N,N,N | B | partly (multi-line) |
| Lead/cycle-time scatter | Time per work item | T,N | B | no |
| Control chart | Is a process stable? | T,N + limits | B | partly (threshold chart) |
| Risk matrix / heat map | Likelihood x impact | C,C,N | A | no |
| Calendar view | Events by day/week | Iv | B | no |
| Work-in-progress run chart | WIP over time | T,N | C | yes (line) |
| Team capacity heat map | Who is loaded when | C,T,N | B | no |
| Timeline with phases (Priestley) | Overlapping periods | Iv | C | no |

### 1.11 Decision results (voting and ranked choices)

| Chart | Answers | Data shape | Prio | Blinc today? |
|---|---|---|---|---|
| Parliament / seat chart | Seat distribution after a vote | C,N | A | no |
| Ranked-choice round table + bars (instant runoff) | Who is eliminated per round? | rounds,C,N | A | no (bar per round yes, composition no) |
| Round-by-round Sankey (IRV flow) | Where do transferred votes go? | Edge per round,N | B | no |
| Stacked bar of approval (yes/no/abstain) | Result of a yes/no vote | C,N | A | yes |
| Quorum/threshold gauge | Is the quorum reached? | N,N | A | partly (marker) |
| Systemic consensing: resistance bar chart | Which option has least resistance? | C,N (0 to 10 resistance) | A | yes (bar, ordered) ⚠️ domain wording of "resistance" taken from the owner's brief |
| Resistance heat map (participants x options) | Who objects where? | C,C,N | B | no |
| Pairwise (Condorcet) matrix | Who beats whom head to head? | Mat | B | no |
| Preference-rank distribution | How often is each rank given? | C,C(rank),N | B | no (heatmap/stacked) |
| Borda / score bar | Points per option | C,N | A | yes |
| Dot vote board | Distribution of dots | C,N | B | yes (bar) |
| Participation / turnout over time | Who has voted when? | T,N | A | yes |
| Delegation graph (liquid democracy) | Who delegated to whom? | Edge | C | no |
| Venn of supporters | Overlap of groups | S,N | C | no |
| Option/criteria matrix score | Weighted decision matrix | C,C,N | B | no (heatmap) |

### 1.12 Survey results (Likert and others)

| Chart | Answers | Data shape | Prio | Blinc today? |
|---|---|---|---|---|
| Diverging stacked bar (Likert) | Share agreeing vs disagreeing, neutral centred | C(item),C(level),N | A | no |
| 100 % stacked bar (Likert, non-diverging) | Same, simpler | C,C,N | A | no |
| Likert mean / top-2-box bar | One score per item | C,N | A | yes |
| Single-choice bar | Distribution of one answer | C,N | A | yes |
| Multiple-choice bar (counts, not summing to 100 %) | Which options were ticked? | C,N | A | yes |
| Pie/donut for yes/no | Binary split | C,N | A | yes |
| Ranking question: stacked rank counts | How was each item ranked? | C,C(rank),N | B | no |
| Matrix question heat map | Items x scale levels | C,C,N | A | no |
| Net promoter score gauge + stacked bar | Promoters/passives/detractors | N,N,N | B | no |
| Slider/numeric question histogram | Spread of answers | Dist | A | yes |
| Cross-tab chart (grouped/stacked by segment) | Answers by group | C,C,N | A | partly |
| Response over time (funnel/timeline) | When did people answer; drop-off? | T,N | A | yes |
| Completion funnel | Where do respondents leave? | C ordered,N | B | no |
| Word cloud / frequency list (free text) | Common themes | term,N | B | no |
| Semantic differential (dumbbell/profile) | Position on bipolar scales | C,N | C | no |
| Radar profile per segment | Compare segment profiles | C,N | B | no |
| Choice map (geographic response) | Answers by region | G,N | C | no |
| Dot plot with confidence interval | Uncertain survey estimate | C,N,N,N | C | no |

### 1.13 Status and KPI

| Chart | Answers | Data shape | Prio | Blinc today? |
|---|---|---|---|---|
| KPI card / stat tile (number + delta) | What is the value now, and how did it change? | N,N | A | no ⚠️ (not a chart in `cn`; may exist as another component) |
| Sparkline in KPI | Trend context | T,N | A | yes |
| Gauge / dial | Value against range | N + range | A | no |
| Progress bar / ring | Share complete | N | A | no in chart module (a separate `progress` primitive exists in our docs) |
| Bullet chart | See 1.1 | | A | partly |
| Traffic-light / RAG status | Healthy, warning, critical | C(state) | A | partly (band colours) |
| Thermometer | Fundraising progress | N,N | C | no |
| Speedometer with thresholds | Threshold zones | N + bands | B | no |
| Status timeline (uptime strip) | When was a service up? | T,state | B | no |
| Heatmap of status (host x time) | Pattern of failures | C,T,state | B | no |
| Scorecard table with in-cell bars | Many KPIs at a glance | R | A | no (table feature) |
| Comparison to baseline | Current vs previous period | C,N,N | A | yes (`comparison_bar_chart`) |
| Threshold line with bands | Budget vs actual | T,N + bands | A | yes |
| Pictorial/emoji rating | Stars | N | C | no |
| Clock / watch-style (custom) | Time-of-day pattern | T | C | no |

### 1.14 Statistics

| Chart | Answers | Data shape | Prio | Blinc today? |
|---|---|---|---|---|
| Boxplot | See 1.3 | | A | no |
| Error bars / error band | Uncertainty | C,N,N,N | B | no |
| Regression / LOESS | Fitted relationship | N,N | B | no |
| Q-Q plot | See 1.3 | | C | no |
| Control chart (X-bar, p-chart) | Process stability | T,N + limits | B | partly |
| Pareto chart | Which few causes dominate? | C,N sorted + cumulative % | B | no |
| Residual plot | Model fit | N,N | C | no |
| Scree plot | Importance of components | C,N | C | no |
| Funnel plot (meta-analysis) | Bias | N,N | C | no |
| Forest plot | Effects with intervals | C,N,N,N | C | no |
| Top-K plot (with "others") | Largest items, rest grouped | C,N | B | no |
| Kaplan-Meier / survival curve | Time to event | T,N | C | no |
| Bland-Altman | Method agreement | N,N | C | no |
| Probability density / CDF | See 1.3 | | B | no |
| Mean with CI dot plot | Compare estimates | C,N,N,N | B | no |

### 1.15 Finance

| Chart | Answers | Data shape | Prio | Blinc today? |
|---|---|---|---|---|
| Candlestick (OHLC) | Price movement per period | T,N,N,N,N | B | no |
| OHLC bars | Same | T,N x4 | C | no |
| Waterfall (profit bridge) | From revenue to profit | C,N signed | A | no |
| Budget vs actual (bar + marker) | Over or under budget? | C,N,N | A | yes |
| Variance chart | Difference to plan | C,N | A | yes (`comparison_bar_chart`) |
| Cumulative / S-curve | Spend or revenue over time | T,N | A | yes (line) |
| Break-even chart | Where costs meet revenue | N,N,N | C | partly (lines) |
| Pareto (ABC analysis) | Which items make most value? | C,N | B | no |
| Aging bucket bars (receivables) | How old are open invoices? | C(bucket),N | A | yes |
| Cash-flow chart | In- and out-flows plus balance | T,N signed | A | partly (stacked bar) |
| Treemap of spend | Where does money go? | Tree,N | B | no |
| Sankey of money flow | Income to expense paths | Edge,N | B | no |
| Moving-average / Bollinger band overlay | Price trend and volatility | T,N | C | no |
| Volume bars with price | Price and volume | T,N,N | C | no |
| Yield curve / term structure | Rate by maturity | C,N | C | yes (line) |
| Depth chart (order book) | Market depth | N,N | C | no |
| Renko / point-and-figure ⚠️ | Price moves, time-free | T,N | C | no |
| Inventory/ABC-XYZ matrix | Value vs variability | C,C | C | no |

### 1.16 Uncategorised / meta types (placed here to keep the list complete)

| Chart | Answers | Data shape | Prio | Blinc today? |
|---|---|---|---|---|
| Table with embedded charts (heat-table, data bars) | Numbers plus pattern | R | A | no (table component) |
| Small multiples / trellis | See 1.1 | | B | no |
| Dashboard layout | Several charts together | n/a | A | not a chart (see `dashboard` docs) |
| Clock / radial time chart | Time-of-day load | T,N | C | no |
| Parallel-coordinate interactive | Brush many dimensions | R | C | no |
| 3-D bar / surface / volume | Three-axis data | N,N,N | C | no |
| Custom/escape-hatch series | Anything the catalogue lacks | any | B | no |

### 1.17 Caveats the catalogue should carry (from From Data to Viz)

Order data, no cut Y axis for bars, spaghetti charts, pie limits, histogram bin size, boxplots hide shape, error bars on bars, overplotting, rainbow palettes, counter-intuitive design. These belong in plugin metadata as warnings and accessibility notes, not as chart types.

### 1.18 Count and priority summary

See the final "Counts" block at the end of this file, produced by script from the tables above.

## 2. What Blinc has

### 2.1 In code (`blinc_cn/src/components/chart/`, Blinc workspace version 0.6.0, Apache-2.0 per its Cargo.toml)

Files: `mod.rs`, `view.rs` (builder `ChartBuilder`), `plot.rs` (geometry and drawing), `pie.rs`, `extras.rs`, `math.rs` (ticks, number format, monotone cubic), `ease.rs` (easing between data updates).

Public entry points:

| Function | Kind |
|---|---|
| `line_chart()` | multi-series line, optional dots, curve Linear/Smooth(default)/Step |
| `area_chart()` | filled line, stackable |
| `bar_chart()` | grouped bars, `.stacked()`, `.horizontal()` |
| `spark_line(values)` | axis-less trend, `.filled()` |
| `threshold_line_chart()` | line against `ChartBand`s, dots take band colour, `.baseline()` |
| `histogram(values)` | equal-width bins, `.bins()`, `.log_scale()`, `.marker()` |
| `comparison_bar_chart()` | paired baseline/current bars with signed change note and `.threshold()` |
| `pie_chart()` | pie, `.donut(hole)`, `.total(caption)`, legend, tooltip |

Options: `series`/`data` (Signal or Computed reactive), `labels`, `height`, `width`, `curve`, `dots`, `stacked`, `horizontal`, `no_grid`, `no_axes`, `legend`, `no_tooltip`, `format` (callback), `min`, `max`, `color`, `band`, `marker`, `gap`, `class`. Data types: `ChartSeries {name, values: Vec<f64>, color}`, `ChartBand`, `ChartMarker`, `PieSlice`, `ComparisonItem`. Features: hover tooltip, easing animation to new data, colours from `--chart-1`..`--chart-5` tokens.

Data model limits seen in the code: one numeric value axis; categories only as string labels (no time axis, no numeric x axis, no log axis except histogram counts); no negative-value handling documented for bars ⚠️ (I did not trace the drawing code for it); reactive Rust builders, no serialisable spec.

Accessibility in code: a search for `aria`, `role`, `alt` in the chart module found nothing. The chart is drawn on a canvas with a tooltip; no text alternative or data table was found.

### 2.2 In our docs (`docs/en/components/widgets/data/chart/`)

Promised: variants `line`, `bar`, `pie`, `doughnut`, `scatter`, `heatmap`, `radar`; attributes `data`, `type`, `interactive`, `showLegend`, `showTooltip`, `showGrid`, `animate`, `animationDuration` (default 1000 ms), events `onHover`, `onDataChange`, `role=img`, `labels`/`values`/`colors`; gestures tap/drag/pinch/swipe; export; states `leer`/`wartend`; always offer a numeric alternative (table); responsive legend moving below; grouping of too many points.

### 2.3 Conflicts

| Topic | Docs | Code |
|---|---|---|
| Scatter, heatmap, radar | promised | absent |
| Area, sparkline, histogram, threshold, comparison, stacked, horizontal | not mentioned | present |
| API shape | one `Chart` with `type` string and `data` array | separate builder functions per kind, typed Rust |
| `showLegend`/`showTooltip`/`showGrid` | booleans | `.legend(bool)`, `.no_tooltip()`, `.no_grid()` |
| `animationDuration` | configurable | not exposed (easing in `ease.rs`; I did not check a fixed duration) |
| `onHover`, `onDataChange` events | listed | none found; hover is internal, data changes via reactive signal |
| Export | listed | none found |
| Pinch/drag zoom | described | none found |
| `role=img` / aria-label / numeric alternative | required | none found |
| Colours | "white background, grey grid" | CSS tokens `--chart-1..5`, `--cn-chart-*` |
| Usage examples | JSX placeholder, flagged to be replaced | Rust builder |

Conclusion: the docs describe a single declarative `Chart` (close to a spec format), the code is a set of imperative builders. Adopting a standard interface would resolve the conflict in favour of the docs' shape.

## 3. Interface standard candidates

Goal: one chart interface with data separated from presentation, usable from Rust, serialisable (for plugins, storage, diffing).

| Candidate | Published spec? | Licence | Completeness | Rust implementations |
|---|---|---|---|---|
| **Vega-Lite** | Yes: JSON Schema at `https://vega.github.io/schema/vega-lite/v6.json`, docs describe `data`, `transform`, `params`, `mark`, `encoding`, composition (layer/facet/concat/repeat) | BSD-3-Clause (repo) | High for statistical and business charts; marks: area, bar, circle, line, point, rect, rule, square, text, tick, geoshape, arc, image, trail, boxplot, errorband, errorbar. Weak or absent: Gantt (can be built from bar+rule), gauge, treemap/Sankey/network (those need Vega), parliament, funnel, candlestick (buildable with rule+bar) | `vega_lite_4` (typed structs from the schema, targets v4 only, last release seen Apr 2023 per search snippet); `vl-convert-rs` (renders to SVG/PNG/PDF via embedded V8 running the JavaScript compiler/renderer, BSD-3-Clause). No native Rust compiler or renderer found ⚠️ |
| **Vega** (lower layer) | Yes, JSON; gallery covers tree, treemap, sunburst, circle packing, force layout, edge bundling, arc diagram, word cloud, beeswarm, maps, contours, parallel coordinates | BSD-3-Clause ⚠️ (Vega-Lite repo page shows BSD-3; Vega repo not fetched) | Highest of the grammar options; imperative-ish (scales, marks, signals) | Same as above (vl-convert handles Vega) |
| **Grammar of Graphics** (Wilkinson) | A book/theory, not a machine-readable spec | n/a | Concepts: data, transformation, scales, coordinate systems, geometries, guides. It underlies Vega-Lite, ggplot2, Plot | n/a. Vega-Lite and Plot are implementations of the idea |
| **Apache ECharts option** | De-facto format with a very large documented option reference (series types per `llms.txt`: bar, boxplot, candlestick, chord, custom, effectScatter, funnel, gauge, graph, heatmap, line, lines, map, parallel, pictorialBar, pie, radar, sankey, scatter, sunburst, themeRiver, tree, treemap; plus GL series). Formal JSON Schema not seen; TypeScript types exist (`index.d.ts`) ⚠️ | Apache-2.0 | Broadest ready-made catalogue. Mixes data and style in `series`; has `dataset` and `encode` to separate data | `charming` (Apache-2.0 OR MIT; typed builders; renders via browser HTML, embedded deno_core SSR to SVG/PNG, or wasm). Needs a JavaScript engine to draw |
| **Observable Plot** | No formal spec found; JavaScript API with documented marks | ISC | Good for exploratory charts; not serialisable by design ⚠️ (API is function calls) | none found ⚠️ |
| **Plotly schema** | `plot-schema.json` exists in plotly.js ⚠️ (page did not mention it) | MIT | Large trace set (statistical, financial, maps, 3D) | `plotly.rs` (MIT; Rust builders that emit HTML for plotly.js) ⚠️ |
| **Apache Arrow** (data side) | Columnar format spec is published ⚠️ (arrow.apache.org, not fetched) | Apache-2.0 (arrow-rs repo) | A transport for tables, not a chart description; typed columns, zero-copy | `arrow-rs` (official) |
| **Tidy data** (Wickham 2014) | Paper, a rule set: one variable per column, one observation per row, one table per observational unit ⚠️ | n/a | A discipline, not a format; fits Vega-Lite encoding exactly | n/a |
| **WAI-ARIA Graphics Module 1.0** | W3C Recommendation, 2 Oct 2018 | W3C document licence ⚠️ | Roles `graphics-document`, `graphics-object`, `graphics-symbol`; accessible name required on document and symbol; nested navigation | n/a (a web standard, but its model of nested labelled objects can be copied) |

### Accessibility requirements (to be part of the interface regardless of base)

From the Graphics module: chart = `graphics-document` with an accessible name; data points or series = `graphics-object`/`graphics-symbol`; hierarchy navigable. From our own docs: always a numeric alternative (table), `role=img` with label. Therefore every chart spec needs: `title`, `description` (long text alternative), per-series names, optional data table fallback, colour-independent encoding (shape, pattern or label) ⚠️ (this last item is a general WCAG-style practice, not from the module text).

### Recommendation

**Use Vega-Lite as the base vocabulary for the data/encoding layer, keep it as a subset we validate against its JSON Schema, and add our own small extension block for what it lacks. Do not adopt the JavaScript runtime.**

Reasons:
1. It is the only candidate that is a published, versioned, machine-validatable spec (JSON Schema) with a strict data/encoding split and a permissive licence (BSD-3-Clause, compatible with MIT OR Apache-2.0 use of the schema as an input format ⚠️ legal check recommended).
2. Rust side is thin: only typed bindings for old v4 and a V8-based renderer. So we must implement our own interpreter in Rust that maps a spec subset to Blinc drawing. That is the real cost and cannot be avoided with any candidate (ECharts via `charming` and Vega via `vl-convert` both require a JS engine, unacceptable for a pure-Rust GUI goal ⚠️ if "100 % Rust" excludes embedded V8; owner to confirm).
3. It does not cover our priority-A set: Gantt, gauge, parliament, risk matrix, KPI card, waterfall (waterfall and Gantt are buildable but awkward). Therefore we need our own **mark/chart-type registry** beside the Vega-Lite subset: plugins declare either a `vega-lite` subset spec or a `custom` type with its own schema.
4. Data side: use plain tidy rows (JSON or Arrow record batches) as the single data shape; Arrow only as optional transport for large tables.

Alternative if the owner wants no foreign spec: define our own (grammar-of-graphics shaped, tidy data + encoding channels + accessibility block) and make Vega-Lite import a plugin. This costs more design work but avoids tracking a spec we do not control. Not recommended unless version churn (v4 to v6 already) becomes painful.

⚠️ Not evaluated: Vega-Lite's own accessibility output (`description`, ARIA attributes in its SVG renderer), the Vega repo licence file, ECharts `aria` option, Plotly schema contents, completeness of any Rust crate beyond README level.

## 4. Plugin shape (input for a later decision)

### 4.1 What a chart plugin declares

- `id`, `version`, `title` (translatable), `purpose` tags from section 1 (compare, part-of-whole, ...).
- **Data contract**: list of required and optional fields with role and type, e.g. `category: C`, `value: N`, `time: T`, `group: C?`; cardinality limits (e.g. pie recommended at most 5 categories); accepted transforms (sort, bin, aggregate) so the host can prepare data.
- **Options schema**: JSON Schema (or WIT record) for presentation options with defaults; separated from data; theme tokens referenced by name, not literal colours.
- **Capabilities**: interactions (hover, select, brush, zoom), animation, export (SVG/PNG/CSV), supported sizes, minimum size.
- **Accessibility block (mandatory)**: accessible name template, long description generator, data-table fallback, keyboard navigation model (what graphics-object nesting it exposes), colour-independent encoding flag.
- **Quality warnings** (from 1.17) shown to authors.
- **Preview/sample data** for a catalogue UI.

### 4.2 Execution models (Rust has no stable ABI)

| Model | Isolation | Cost to render | Fit |
|---|---|---|---|
| In-process (dylib via `abi_stable`-style or static feature crate) | none; a crash kills the host | lowest; draws directly through Blinc `DrawContext` | Only for built-in charts (compiled in). Runtime hot-plugging of dylibs is fragile because the Rust ABI is unstable; `abi_stable` or a C ABI would be required ⚠️ (not evaluated) |
| Separate process + Cap'n Proto (`capnp-rpc`, MIT, zero-copy readers) | strong (OS process, can sandbox) | per update: serialise data and options, receive result; no GPU access | Good isolation and language freedom; extra process management; shared-memory data transfer possible but not verified ⚠️ |
| WASM component (WIT worlds, canonical ABI) | strong, capability-based | similar to process but in-process runtime; call overhead small; no direct GPU either | Typed interface independent of Rust ABI; hot-load without restart; needs a runtime (e.g. wasmtime ⚠️ not evaluated) and the component model's maturity (WASI 0.2/0.3 status not verified) |

### 4.3 Can a plugin return a scene description?

Yes, and this is the pragmatic answer for both out-of-process and WASM: **the plugin does not draw; it returns a retained scene**. The host owns the GPU canvas.

- Scene = flat or tree list of primitives: rect, rounded rect, path (move/line/cubic/close), arc, text (string, font token, anchor), image reference, group with transform and clip; fill/stroke as theme tokens or literals; plus, per object, an accessibility node (role, name, value) and a hit-test id.
- Interactions: the host does hit-testing against the scene, sends back `hover(id)`, `select(id)`, `brush(rect)`; the plugin returns a scene delta (or the whole scene; charts are small).
- This is the same idea as Vega's scenegraph (vl-convert can output scenegraphs per its README, so the concept exists in the Vega ecosystem), and as Blinc's own draw calls (`DrawContext`, `Path`) ⚠️ (I did not check that the Blinc primitives cover everything above).
- Cost: for typical dashboards (hundreds to a few thousand marks) a binary scene is small; encoding as Cap'n Proto or WIT lists is cheap. Heavy cases (100k-point scatter, dense maps) need either decimation in the plugin (aggregate to bins) or a "point cloud" primitive that the host draws as a batch ⚠️ no measurement done.
- Animation: host interpolates between two scenes when node ids match (the existing `ease.rs` idea), so plugins stay stateless.
- Text measurement is the awkward part: layout of axis labels needs font metrics the host owns. Options: plugin asks the host (round trip), or host exposes a `measure_text` import (WASM) or the scene allows anchored labels the host lays out. Needs a decision.
- Alternative for pure declarative plugins: no code at all, only a Vega-Lite subset spec; the host's own Rust interpreter turns it into a scene. This covers the simple 80 % and removes the plugin ABI question for them.

### 4.4 Suggested decision order (not a decision)

1. Fix the data contract and accessibility block (needed in every option).
2. Fix the scene format (needed in every option except in-process).
3. Then choose transport; the scene and declaration schemas are identical for process and WASM, so the choice can be postponed or made per plugin class (built-in = in-process, third party = WASM or process).

## Counts

Counted by script over section 1.1 to 1.16: 260 table rows, of which about 20 are cross-references or near-duplicates listed under a second purpose (e.g. Waterfall, Boxplot, Treemap, Cumulative flow). Roughly 235 to 240 distinct chart types ⚠️ (duplicates detected by exact name only; variants such as "Stacked bar" vs "Stacked bar/column" were not merged by hand).

Priority by row: A = 69, B = 82, C = 109.

Priority A (distinct, by purpose):
- Compare: column, bar, grouped bar, ordered bar, bullet, diverging bar, diverging stacked bar.
- Part of whole: pie, donut, stacked bar, 100 % stacked bar, stacked area, waterfall.
- Distribution: histogram, boxplot.
- Time: line, multi-line, smooth/step line, area, sparkline, column over time, threshold line with bands.
- Relationship: scatter, heatmap, quadrant chart.
- Project: Gantt, milestone timeline, burn-down, burn-up, resource load chart, risk matrix.
- Decision: parliament chart, ranked-choice rounds, approval stacked bar, quorum gauge, resistance bar, Borda/score bar, turnout over time.
- Survey: Likert diverging stacked bar, 100 % stacked Likert, matrix heat map, single/multiple-choice bar, cross-tab chart, response over time.
- Status/KPI: KPI card, gauge, progress bar/ring, RAG status, scorecard with in-cell bars, comparison to baseline.
- Finance: budget vs actual, variance, S-curve, aging buckets, cash flow, waterfall bridge.

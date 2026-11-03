# primitives – building blocks

Cannot be broken down further: one value, one gesture, one state. No band
contains content it only receives at runtime. Test question: *cannot be broken
down further*.

## Type groups (5) — 34 components

### [basics](./basics/) — fundamentals (4)

The fundamentals all other components start from: the base class with its
inherited attributes, states and tokens, plus the smallest building blocks.

[kbd](./basics/kbd/), [label](./basics/label/), [link](./basics/link/), [separator](./basics/separator/)

### [actions](./actions/) — actions (3)

Action elements trigger a single action or bundle actions that belong together.
They change data or states, but not the address.

[button](./actions/button/), [button-group](./actions/button-group/), [floating-action-button](./actions/floating-action-button/)

### [feedback](./feedback/) — feedback (7)

Elements that make the state of an application visible: messages, progress,
loading states and markings.

[alert](./feedback/alert/), [badge](./feedback/badge/), [empty-state](./feedback/empty-state/), [progress](./feedback/progress/), [skeleton](./feedback/skeleton/), [spinner](./feedback/spinner/), [toast](./feedback/toast/)

### [fields](./fields/) — fields (18)

Elements for entering and choosing values. The field (`field`) holds the label,
help text and error message together.

[checkbox](./fields/checkbox/), [color-input](./fields/color-input/), [combobox](./fields/combobox/), [date-input](./fields/date-input/), [field](./fields/field/), [input-group](./fields/input-group/), [mention-input](./fields/mention-input/), [number-input](./fields/number-input/), [otp-input](./fields/otp-input/), [radio-group](./fields/radio-group/), [rating](./fields/rating/), [search-field](./fields/search-field/), [select](./fields/select/), [slider](./fields/slider/), [switch](./fields/switch/), [tags-input](./fields/tags-input/), [text-input](./fields/text-input/), [textarea](./fields/textarea/)

### [media](./media/) — media (2)

Elements that play or show media. `media-player` is the parent class of `audio`
and `video`.

[icon](./media/icon/), [image](./media/image/)

## See also

- [Component overview](../index.md)
- [Base class](./basics/base.md)
- [widgets](../widgets/) – building blocks with known content
- [workbenches](../workbenches/) – open work surfaces
- [Gestures](../../interactions/gestures/) and [Animations](../../interactions/animations/)

# fields

Band [widgets](../) – knows its contents when it is built.

Elements for entering and selecting values. The field (`field`) holds the label, help
text and error message together.

## Elements

- [**date-picker**](./date-picker/) – the date picker opens a calendar overlay in which a date or a range is selected.
- [**emoji-picker**](./emoji-picker/) – an emoji picker is an emoji selection for chat/comments.
- [**file-upload**](./file-upload/) – a file upload is an element for choosing and uploading files.
- [**range-calendar**](./range-calendar/) – the range calendar selects one continuous period of time.
- [**time-picker**](./time-picker/) – the time picker selects a time of day from a list of possible times.

## Profiles

| Component | Inherits from | Variants | Role | Status |
|-----------|---------------|----------|------|--------|
| [date-picker](./date-picker/) | `base`, `date-input` | `einzeln`, `bereich`, `wiederkehrend` | `dialog` | documented |
| [emoji-picker](./emoji-picker/) | `base` | `inline`, `overlay`, `reaktion` | - | documented |
| [file-upload](./file-upload/) | `base` | `File Picker`, `Drag & Drop`, `Image Preview` | - | documented |
| [range-calendar](./range-calendar/) | `base`, `date-picker` | `zwei-monate`, `ein-monat` | `dialog` | documented |
| [time-picker](./time-picker/) | `base`, `date-input` | `liste`, `ziffernblatt` | `listbox` | documented |

## See also

- [Component overview](../../index.md)
- [Band widgets](../)
- [Base component](../../primitives/basics/base.md)

# <Live API Namespace>

## <Class>

General class description.

### Sources

- **Primary:** `Live/classes/<Class>.py` (stub dump)
- **Secondary:** `MaxForLive/<class>.md`
- **Probes:** `<links to probe scripts/logs or notes>` or `None`

### Probe Notes

- `<finding>`

### Open Questions

- `<unknown behavior to probe later>`

### Children

| Child          | Returns  | Shape           | Access  | Listenable | Available Since    | Summary               |
| -------------- | -------- | --------------- | ------- | ---------- | ------------------ | --------------------- |
| `<child_name>` | `<type>` | `<single/list>` | `<get>` | `<yes/no>` | `<version or N/A>` | `<short description>` |

#### `<child_name>`

- **Returns:** `<type>`
- **Shape:** `<single/list>`
- **Access:** `<get>`
- **Listenable:** `<yes/no>`
- **Applicable to:** `<all | midi/audio/group/return/master>`
- **Available Since:** `<version or N/A>`
- **Sources:** `<stub | max | probe>`
- **Probe Status:** `<unprobed | partial | verified>`

**Description:**
Full multiline description including quirks/constraints.

### Properties

| Property          | Get Returns | Set Accepts   | Listenable | Available Since    | Summary               |
| ----------------- | ----------- | ------------- | ---------- | ------------------ | --------------------- |
| `<property_name>` | `<type>`    | `<type or —>` | `<yes/no>` | `<version or N/A>` | `<short description>` |

#### `<property_name>`

- **Get Returns:** `<type>`
- **Set Accepts:** `<type>` or —
  - **Undo-tracked:** `<yes/no/Unknown>`
  - **Async visibility:** `<immediate | next_tick | variable | Unknown>`
- **Listenable:** `<yes/no>`
- **Applicable to:** `<all | midi/audio/group/return/master>`
- **Available Since:** `<version or N/A>`
- **Sources:** `<stub | max | probe>`
- **Probe Status:** `<unprobed | partial | verified>`

If `Set Accepts` is — (read-only), omit the nested set metadata bullets.

**Description:**
Full multiline description including quirks/constraints.

### Methods

| Signature               | Returns  | Available Since    | Summary               |
| ----------------------- | -------- | ------------------ | --------------------- |
| `<method_name>(<args>)` | `<type>` | `<version or N/A>` | `<short description>` |

#### `<method_name>(<args>)`

- **Returns:** `<type>`
- **Args:** `<arg_name>: <type> = <default>` (repeat as needed)
- **Raises/Errors:** `<description or Unknown>`
- **Applicable to:** `<all | midi/audio/group/return/master>`
- **Undo-tracked:** `<yes/no/Unknown>`
- **Side Effects:** `<describe primary mutation in one line>`
- **Async visibility:** `<immediate | next_tick | variable | Unknown>`
- **Available Since:** `<version or N/A>`
- **Sources:** `<stub | max | probe>`
- **Probe Status:** `<unprobed | partial | verified>`

**Description:**
Full multiline description including quirks/constraints.

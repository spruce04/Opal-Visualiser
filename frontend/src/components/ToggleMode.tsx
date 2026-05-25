//Toggle mode between total and net taps
//Accept the toggle_taps function from App.tsx as a param
//Call it with a param to set the new display mode

interface ToggleModeProps {
    on_toggle: (mode: string) => void;
    active_mode: string;
  }

export default function ToggleMode({on_toggle, active_mode}: ToggleModeProps) {
    //Give the active diplay button(s) the active class
    function getClassName(mode): string {
        if (mode == active_mode) {
            return mode + " active";
        }
        return mode;
    }

    return (
        <div className="toggleMode">
            <p>Select Display Mode:</p>
            <button className={getClassName("total_taps")} onClick={() => on_toggle("total_taps")}>Total Taps</button>
            <button className={getClassName("net_taps")} onClick={() => on_toggle("net_taps")}>Net Taps (tap on-tap off)</button>
        </div>
    );
}
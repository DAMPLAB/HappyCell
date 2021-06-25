<script>
import SVG from "@yapv/svg";

export default {
  functional: true,
  render(h, context) {
    const MarkerComponent = SVG.circular.MarkerComponent(h);
    return MarkerComponent(context.props, context.children);
  }
};
</script>

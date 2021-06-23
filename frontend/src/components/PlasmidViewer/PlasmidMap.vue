<script>
import SVG from "@yapv/svg";

export default {
  functional: true,
  render(h, context) {
    const PlasmidMap = SVG.circular.PlasmidMapComponent(h);
    return PlasmidMap(context.props, context.children);
  }
};
</script>

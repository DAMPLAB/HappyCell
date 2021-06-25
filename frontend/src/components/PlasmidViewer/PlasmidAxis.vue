<script>
import SVG from '@yapv/svg';

export default {
	functional: true,
	render (h, context) {
		const AxisComponent = SVG.circular.AxisComponent(h);
    return AxisComponent(context.props, context.children);
	}
}
</script>
